# How It Works

1. **Set Memory Size:**
   - Enter the total memory size (e.g., `100`) and click **Set Memory** to initialize the memory block.
   - The program displays the initial memory as a single free block.

2. **Allocate Memory:**
   - Enter a **Process ID** (e.g., `A`) and the **Memory Size Needed** (e.g., `30`).
   - Click **Allocate (First-Fit)** or **Allocate (Best-Fit)** to assign memory.
   - The memory gets allocated according to the selected algorithm, and the memory state updates.

3. **Deallocate Memory:**
   - Enter a **Process ID** and click **Deallocate** to free memory assigned to that process.
   - The system merges adjacent free blocks automatically to optimize memory usage.

---

# Algorithms Used

- **First-Fit:**
  - Scans the memory from the beginning and allocates the first available block that is large enough for the process.
  - If the block is larger than needed, it splits the block into allocated and free parts.

- **Best-Fit:**
  - Searches the entire memory to find the smallest block that fits the process.
  - Minimizes wasted space but may slow down allocation since it requires scanning the entire memory.

---

# Comparison of Efficiency

| Algorithm  | Time Complexity  | Memory Utilization  |
|------------|----------------|---------------------|
| **First-Fit**  | **O(n)** (Linear Search) | May cause more fragmentation  |
| **Best-Fit**  | **O(n)** (Linear Search) | Reduces fragmentation but may slow down allocation |

