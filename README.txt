README - My Mini Computer (25-bit CPU in Logisim)
==================================================

📌 PROJECT OVERVIEW
--------------------
This project implements a fully functional **25-bit CPU** using Logisim, designed and built as part of a university-level computer architecture course.

The system features:
- A custom **Instruction Set Architecture (ISA)** with 16 instructions
- A **Hardwired Control Unit** with FSM logic
- An **ALU** supporting arithmetic and logic operations
- A structured **register set** including PC, IR, MAR, MBR, and PLR
- A shared **25-bit system bus**
- A **compiler GUI in Python** to write and compile assembly instructions into Logisim-readable hex machine code (`instruction.img`)

Designed and developed by: **Utsa Roy (Roll: 2207027)**  
Course: CSE 2114 - Computer Architecture and Organization  
University: Khulna University of Engineering & Technology (KUET)


🧠 FEATURES
------------
✅ 25-bit architecture  
✅ Custom 16-instruction ISA  
✅ Modular and scalable Logisim circuit (.circ)  
✅ Python GUI Compiler for user-friendly code writing & compilation  
✅ Support for variables and memory initialization  
✅ Line-numbered editor with syntax support  
✅ Instruction hex image generation for Logisim RAM  

🔧 MAIN COMPONENTS
-------------------
- **ALU**: Handles arithmetic (ADD, MUL, NEG, etc.) and logical (AND) operations
- **Registers**: 
  - `ACC`: Accumulator
  - `PC`: Program Counter
  - `IR`: Instruction Register
  - `MAR`: Memory Address Register (6-bit)
  - `MBR`: Memory Buffer Register (25-bit)
  - `PLR`: Parallel Load Register for privilege level
- **Control Unit**: Finite State Machine that manages fetch-decode-execute cycle
- **Memory**: 64 addressable memory locations, 25-bit wide


🧾 INSTRUCTION SET SUMMARY
---------------------------
| Opcode | Mnemonic | Definition                                 |
|--------|----------|---------------------------------------------|
| 0000   | AND      | ACC ← ACC & M[address]                     |
| 0001   | ADD      | ACC ← ACC + M[address]                     |
| 0002   | STO      | M[address] ← ACC                           |
| 0003   | BUN      | PC ← M[address]                            |
| 0004   | BSB      | M[address] ← PC, PC ← M[address] + 1       |
| 0005   | LOAD     | ACC ← M[address]                           |
| 0006   | ISZ      | M[address]++, PC++ if M=0                  |
| 0007   | JZ       | Jump if ACC = 0                            |
| 0008   | PUSH     | ACC ← Stack                                |
| 0009   | POP      | Stack → ACC                                |
| 000A   | HALT     | Stop execution                             |
| 000B   | NEG      | ACC ← -ACC                                 |
| 000C   | MUL      | ACC ← ACC × M[address]                     |
| 000D   | DIV      | ACC ← ACC ÷ M[address]                     |
| 000E   | REM      | ACC ← ACC % M[address]                     |
| 000F   | JN       | Jump if ACC < 0                            |


💻 COMPILER GUI (Compiler.py)
------------------------------
A Python Tkinter-based GUI allows you to:
- Write pseudo-assembly instructions
- Save/load text files
- Compile to machine-readable `instruction.img` for Logisim RAM
- View supported opcodes & keyboard shortcuts

🔑 Shortcuts:
- Ctrl + N: New File
- Ctrl + O: Open File
- Ctrl + S: Save File
- Ctrl + Space: Compile


📂 FILE STRUCTURE
-------------------
My-Tiny-Computer/
│
├── My mini computer 2207027.circ     # Main Logisim CPU circuit
├── Compiler.py                       # Python GUI compiler
├── Documentation.pdf  # Project report and documentation
├── instruction.img                   # Output of compiled code (generated)
└── README.txt                        # This file


📌 EXAMPLE: SIMPLE ADDITION
----------------------------
; Adds content of memory[4] and memory[5], stores result in memory[8]

load 4         ; ACC ← M[4]
add 5          ; ACC ← ACC + M[5]
sto 8          ; M[8] ← ACC
halt           ; Stop execution

var 4 2        ; Memory[4] = 2
var 5 3        ; Memory[5] = 3

🛠 Compiles to (RAM format):
v2.0 raw
0500004 0100005 0200008 0a00000 0000002 0000003


📌 EXAMPLE: ISZ (Increment and Skip if Zero)
--------------------------------------------
isz 6
halt

var 6 0


📈 HOW TO RUN
--------------
1. Open `My mini computer 2207027.circ` in Logisim
2. Load the compiled hex (`instruction.img`) into the RAM
3. Start simulation (toggle clock or run with manual step)
4. Watch registers and buses to follow execution

📝 REFERENCES
--------------
- Logisim Tool (http://www.cburch.com/logisim/)
- Course Lectures and Instructor Notes
- Custom compiler developed with Tkinter in Python


📬 CONTACT
------------
Author: Utsa Roy  
GitHub: https://github.com/utsaroy  
