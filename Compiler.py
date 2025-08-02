import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Compiler for Utsa's Tiny Computer")
        self.root.geometry("600x400")

        # Create a frame to hold the line numbers and text area
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        # Create a Text widget for line numbers
        self.line_numbers = tk.Text(self.frame, width=4, padx=5, pady=5, takefocus=0, border=0, background='lightgrey', state='disabled')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Create a Text widget for the main text area
        self.text_area = tk.Text(self.frame, wrap="word", undo=True)
        self.text_area.pack(side=tk.LEFT, expand=True, fill="both")

        # Set focus to the text area
        self.text_area.focus_set()

        # Bind the text area to update line numbers on any change
        self.text_area.bind("<KeyRelease>", self.update_line_numbers)
        self.text_area.bind("<MouseWheel>", self.update_line_numbers)
        self.text_area.bind("<Button-1>", self.update_line_numbers)

        # Bind Ctrl+S to save the file
        self.root.bind('<Control-s>', lambda event: self.save_file())
        self.root.bind('<Control-o>', lambda event: self.open_file())
        self.root.bind('<Control-n>', lambda event: self.new_file())
        self.root.bind('<Control-space>', lambda event: self.write_compiled_code())

        # Create a Menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        # Compile command directly on menu bar
        self.menu_bar.add_command(label="Compile", command=self.write_compiled_code)

        # Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Opcodes", command=self.show_opcodes)
        self.help_menu.add_command(label="Shortcuts", command=self.show_shortcuts)

        # about menu
        self.menu_bar.add_command(label="About", command=self.about_menu)

    

        # Initialize line numbers
        self.update_line_numbers()
    
    def about_menu(self):
        #about with github link button
        messagebox.showinfo("About", "Compiler for Utsa's Tiny Computer\n\nDeveloped by Utsa Roy\n\nGitHub: github.com/utsaroy\n\n")




    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.update_line_numbers()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
        self.update_line_numbers()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def exit_editor(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()


    def show_opcodes(self):
        opcodes_info = """
        Available Opcodes:
        - and: AC = AC AND M[address]
        - add: AC = AC + M[address]
        - sto: M[address] = AC
        - bun: PC = address (Branch Unconditionally)
        - bsb: M[address] = PC; PC = address + 1 (Branch & Save)
        - load: AC = M[address]
        - isz: M[address]++; if (M[address]==0) PC++ (Increment & Skip if Zero)
        - jz: Jump if Zero flag is set
        - push: Push AC onto the stack
        - pop: Pop from stack into AC
        - halt: Stop the clock
        - neg: AC = -AC (Negate Accumulator)
        - mul: AC = AC * M[address] (Multiply)
        - div: AC = AC / M[address] (Divide)
        - rem: AC = AC % M[address] (Remainder)
        - jn: Jump if Negative flag is set
        """
        messagebox.showinfo("Opcodes", opcodes_info)

    def show_shortcuts(self):
        shortcuts_info = """
        Keyboard Shortcuts:
        - Ctrl+N: New File
        - Ctrl+O: Open File
        - Ctrl+S: Save File
        - Ctrl+Space: Compile Code
        """
        messagebox.showinfo("Shortcuts", shortcuts_info)


    def compile_code(self, input_code):
        instruction_codes = {
        'and' : 0x0000000,
        'add' : 0x0100000,
        'sto' : 0x0200000,
        'bun' : 0x0300000,
        'bsb' : 0x0400000,
        'load' : 0x0500000,
        'isz' : 0x0600000,
        'jz' : 0x0700000,
        'push' : 0x0800000,
        'pop' : 0x0900000,
        'halt' : 0x0a00000,
        'neg' : 0x0b00000,
        'mul' : 0x0c00000,
        'div' : 0x0d00000,
        'rem' : 0x0e00000,
        'jn' : 0x0f00000,
        }

        ram_data = ['']*64
        instructions = input_code.split('\n')
        index = 0
        for instruction in instructions:
            instruction = instruction.strip().lower()
            if instruction == '': continue
            elif instruction and len(instruction.split()) == 1:
                op = instruction
                if op not in instruction_codes:
                    return False
                compiled_instruction = str(hex(instruction_codes[op]))
                compiled_instruction = compiled_instruction[2:].zfill(6)
                if index >= 64:
                    return False
                ram_data[index] = compiled_instruction
                index += 1
            elif instruction and len(instruction.split()) == 2:
                op, arg = instruction.split()
                if op not in instruction_codes:
                    return False
                compiled_instruction = str(hex(instruction_codes[op] + int(arg)))
                compiled_instruction = compiled_instruction[2:].zfill(6)
                if index >= 64:
                    return False
                ram_data[index] = compiled_instruction
                index += 1
            elif instruction and len(instruction.split()) == 3 and instruction.split()[0] == 'var':
                op, address, val = instruction.split()
                compiled_instruction = str(hex(int(val)))
                compiled_instruction = compiled_instruction[2:]
                if index >= 64:
                    return False
                ram_data[int(address)] = compiled_instruction
            # else:
            #     return False
        
        result = 'v2.0 raw\n'
        count_empty = 0
        for data in ram_data:
            if data == '':
                count_empty += 1
            else:
                if count_empty:
                    result += str(count_empty) + '*0 '
                    count_empty = 0
                result += data + ' '
        return result

    def write_compiled_code(self):

        instructions = self.text_area.get(1.0, tk.END).strip()
        compiled_lines = self.compile_code(instructions)

        if not compiled_lines:
            messagebox.showerror("Compile", "Error compiling code!")
            return

        with open("instruction.img", "w") as file:
            file.write(compiled_lines)

        messagebox.showinfo("Compile", "Code compiled successfully and saved to instruction.img")

    def update_line_numbers(self, event=None):
        # Get the number of lines in the text area
        lines = self.text_area.get(1.0, tk.END).count('\n')
        line_numbers_text = "\n".join(str(i) for i in range(0, lines + 1))

        # Update the line numbers widget
        self.line_numbers.config(state='normal')
        self.line_numbers.delete(1.0, tk.END)
        self.line_numbers.insert(tk.END, line_numbers_text)
        self.line_numbers.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()


#pyinstaller --onefile -w filename.py
