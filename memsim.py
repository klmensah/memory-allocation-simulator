import tkinter as tk
from tkinter import messagebox

class MemoryManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Allocation Simulator")

        # Memory Input
        tk.Label(root, text="Total Memory Size:").grid(row=0, column=0)
        self.memory_size_entry = tk.Entry(root)
        self.memory_size_entry.grid(row=0, column=1)

        tk.Button(root, text="Set Memory", command=self.set_memory).grid(row=0, column=2)

        # Process Inputs
        tk.Label(root, text="Process ID:").grid(row=1, column=0)
        self.process_id_entry = tk.Entry(root)
        self.process_id_entry.grid(row=1, column=1)

        tk.Label(root, text="Memory Size Needed:").grid(row=2, column=0)
        self.memory_request_entry = tk.Entry(root)
        self.memory_request_entry.grid(row=2, column=1)

        tk.Button(root, text="Allocate (First-Fit)", command=self.first_fit).grid(row=1, column=2)
        tk.Button(root, text="Allocate (Best-Fit)", command=self.best_fit).grid(row=2, column=2)

        # Deallocation
        tk.Label(root, text="Process ID to Deallocate:").grid(row=3, column=0)
        self.dealloc_process_entry = tk.Entry(root)
        self.dealloc_process_entry.grid(row=3, column=1)

        tk.Button(root, text="Deallocate", command=self.deallocate).grid(row=3, column=2)

        # Memory Display Box
        self.memory_display = tk.Text(root, height=10, width=50)
        self.memory_display.grid(row=4, column=0, columnspan=3)
        self.memory_display.insert(tk.END, "Set memory first.\n")

        self.memory = []

    def set_memory(self):
        """Initialize memory with a single large free block."""
        try:
            size = int(self.memory_size_entry.get())
            self.memory = [(size, None)]  # (block size, allocated process)
            messagebox.showinfo("Success", f"Memory initialized with {size} units.")
            self.display_memory()
        except ValueError:
            messagebox.showerror("Error", "Enter a valid memory size.")

    def display_memory(self):
        """Display the current state of memory."""
        self.memory_display.delete("1.0", tk.END)  # Clear previous output
        output = "Memory Blocks:\n"

        for i, (size, allocated) in enumerate(self.memory):
            status = f"Process {allocated}" if allocated is not None else "Free"
            output += f"Block {i}: Size={size}, Status={status}\n"

        self.memory_display.insert(tk.END, output)
        self.memory_display.update_idletasks()

    def first_fit(self):
        """Allocate memory using the First-Fit strategy."""
        process_id = self.process_id_entry.get()
        try:
            size = int(self.memory_request_entry.get())
            for i, (block_size, allocated) in enumerate(self.memory):
                if allocated is None and block_size >= size:
                    if block_size > size:
                        self.memory[i] = (size, process_id)
                        self.memory.insert(i + 1, (block_size - size, None))
                    else:
                        self.memory[i] = (block_size, process_id)
                    messagebox.showinfo("Success", f"Process {process_id} allocated {size} units (First-Fit).")
                    self.display_memory()
                    return
            messagebox.showerror("Error", f"Process {process_id} cannot be allocated {size} units (First-Fit).")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid memory size.")

    def best_fit(self):
        """Allocate memory using the Best-Fit strategy."""
        process_id = self.process_id_entry.get()
        try:
            size = int(self.memory_request_entry.get())
            best_index = -1
            best_size = float('inf')

            for i, (block_size, allocated) in enumerate(self.memory):
                if allocated is None and block_size >= size and block_size < best_size:
                    best_size = block_size
                    best_index = i

            if best_index != -1:
                block_size, _ = self.memory[best_index]
                if block_size > size:
                    self.memory[best_index] = (size, process_id)
                    self.memory.insert(best_index + 1, (block_size - size, None))
                else:
                    self.memory[best_index] = (block_size, process_id)
                messagebox.showinfo("Success", f"Process {process_id} allocated {size} units (Best-Fit).")
                self.display_memory()
            else:
                messagebox.showerror("Error", f"Process {process_id} cannot be allocated {size} units (Best-Fit).")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid memory size.")

    def deallocate(self):
        """Deallocate memory used by a process and merge free blocks."""
        process_id = self.dealloc_process_entry.get()
        for i, (block_size, allocated) in enumerate(self.memory):
            if allocated == process_id:
                self.memory[i] = (block_size, None)
                messagebox.showinfo("Success", f"Process {process_id} deallocated.")

        # Merge adjacent free blocks
        i = 0
        while i < len(self.memory) - 1:
            if self.memory[i][1] is None and self.memory[i + 1][1] is None:
                self.memory[i] = (self.memory[i][0] + self.memory[i + 1][0], None)
                del self.memory[i + 1]
            else:
                i += 1

        self.display_memory()


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryManagerGUI(root)
    root.mainloop()
