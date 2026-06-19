import tkinter as tk
from tkinter import messagebox

class PDASimulator:
    def __init__(self):
        # ---------------------------------------------------------
        # BAGIAN INI BISA DIMODIFIKASI UNTUK MENGHINDARI PLAGIARISME
        # Default: PDA untuk bahasa a^n b^n (n >= 1)
        # ---------------------------------------------------------
        self.start_state = 'q0'
        self.accept_states = {'qf'}
        self.start_stack = ['Z'] # Z adalah simbol awal stack

        # Aturan transisi format: 
        # (state_sekarang, input_char, top_stack) : [(state_selanjutnya, string_yang_di_push)]
        # Keterangan: Epsilon direpresentasikan dengan string kosong ''
        self.transitions = {
            ('q0', 'a', 'Z'): [('q0', 'aZ')], # Baca 'a', push 'a' ke atas 'Z'
            ('q0', 'a', 'a'): [('q0', 'aa')], # Baca 'a', push 'a' ke atas 'a'
            ('q0', 'b', 'a'): [('q1', '')],   # Baca 'b', pop 'a' (push string kosong)
            ('q1', 'b', 'a'): [('q1', '')],   # Baca 'b', pop 'a'
            ('q1', '', 'Z'): [('qf', 'Z')]    # Transisi epsilon ke state final
        }

    def process_string(self, input_string):
        # Menggunakan Stack untuk simulasi (algoritma DFS) agar bisa menangani Nondeterministic PDA
        # Format elemen: (index_karakter, state_sekarang, kondisi_stack_pda, riwayat_langkah)
        stack = [(0, self.start_state, self.start_stack, [f"Start: State={self.start_state}, Stack={''.join(self.start_stack)}"])]

        while stack:
            index, state, pda_stack, trace = stack.pop()

            # Jika seluruh input sudah dibaca dan berada di Final State
            if index == len(input_string) and state in self.accept_states:
                trace.append(f"✅ String DITERIMA (Accepted) di State {state}")
                return True, trace

            # Ambil karakter saat ini jika belum di ujung string
            current_char = input_string[index] if index < len(input_string) else None
            top_stack = pda_stack[-1] if pda_stack else None

            if not top_stack:
                continue

            # 1. Cek transisi normal (Membaca karakter input)
            if current_char:
                key = (state, current_char, top_stack)
                if key in self.transitions:
                    for next_state, push_str in self.transitions[key]:
                        # Update stack PDA: Pop top, lalu Push karakter baru (urutan terbalik agar sesuai stack)
                        new_stack = pda_stack[:-1] + list(push_str[::-1])
                        step_info = f"Baca '{current_char}', State {state} -> {next_state}, Stack: {''.join(new_stack)}"
                        stack.append((index + 1, next_state, new_stack, trace + [step_info]))

            # 2. Cek transisi Epsilon (Tanpa membaca karakter input)
            eps_key = (state, '', top_stack)
            if eps_key in self.transitions:
                for next_state, push_str in self.transitions[eps_key]:
                    new_stack = pda_stack[:-1] + list(push_str[::-1])
                    step_info = f"Baca 'ε' (Epsilon), State {state} -> {next_state}, Stack: {''.join(new_stack)}"
                    stack.append((index, next_state, new_stack, trace + [step_info]))

        return False, ["❌ String DITOLAK (Rejected)"]


class PDAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDA Automator - Tugas Praktikum #3")
        self.root.geometry("500x550")
        self.root.configure(padx=20, pady=20)
        
        self.pda = PDASimulator()

        # UI Components
        tk.Label(root, text="Mesin PDA: Bahasa aⁿbⁿ", font=("Helvetica", 14, "bold")).pack(pady=5)
        tk.Label(root, text="Masukkan string (hanya huruf 'a' dan 'b'):").pack(anchor="w")

        self.input_entry = tk.Entry(root, font=("Helvetica", 12), width=40)
        self.input_entry.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        
        self.check_btn = tk.Button(btn_frame, text="Cek Keanggotaan", bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), command=self.run_pda)
        self.check_btn.pack(side="left", padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Clear", bg="#f44336", fg="white", font=("Helvetica", 10, "bold"), command=self.clear_ui)
        self.clear_btn.pack(side="left", padx=5)

        # Result display
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
        self.result_label.pack(pady=10)

        # Trace Log
        tk.Label(root, text="Jejak Langkah (Trace Log):").pack(anchor="w")
        self.trace_box = tk.Text(root, height=15, width=55, state="disabled", bg="#f0f0f0")
        self.trace_box.pack(pady=5)

    def run_pda(self):
        input_string = self.input_entry.get()
        
        if not input_string.isalpha() and input_string != "":
            messagebox.showwarning("Input Tidak Valid", "Hanya masukkan huruf (a dan b).")
            return

        is_accepted, trace = self.pda.process_string(input_string)

        # Tampilkan Status
        if is_accepted:
            self.result_label.config(text="STATUS: ACCEPTED ✅", fg="green")
        else:
            self.result_label.config(text="STATUS: REJECTED ❌", fg="red")

        # Tampilkan Trace di Text Box
        self.trace_box.config(state="normal")
        self.trace_box.delete(1.0, tk.END)
        self.trace_box.insert(tk.END, f"Input: '{input_string}'\n")
        self.trace_box.insert(tk.END, "-"*40 + "\n")
        for step in trace:
            self.trace_box.insert(tk.END, step + "\n")
        self.trace_box.config(state="disabled")

    def clear_ui(self):
        self.input_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.trace_box.config(state="normal")
        self.trace_box.delete(1.0, tk.END)
        self.trace_box.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDAApp(root)
    root.mainloop()