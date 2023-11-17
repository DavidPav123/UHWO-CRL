import subprocess

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/k-nucleotide/C/knucleotideC < /workspaces/Rusty-Kernels-Code/k-nucleotide/input.txt ; } 2>> /workspaces/Rusty-Kernels-Code/k-nucleotide/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/k-nucleotide/C/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/k-nucleotide/C/knucleotideC < /workspaces/Rusty-Kernels-Code/k-nucleotide/input.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/k-nucleotide/C++/knucleotideC++ < /workspaces/Rusty-Kernels-Code/k-nucleotide/input.txt ; } 2>> /workspaces/Rusty-Kernels-Code/k-nucleotide/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/k-nucleotide/C++/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/k-nucleotide/C++/knucleotideC++ < /workspaces/Rusty-Kernels-Code/k-nucleotide/input.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/k-nucleotide/Rust/target/release/Rust < /workspaces/Rusty-Kernels-Code/k-nucleotide/input.txt ; } 2>> /workspaces/Rusty-Kernels-Code/k-nucleotide/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/k-nucleotide/Rust/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/k-nucleotide/Rust/target/release/Rust < /workspaces/Rusty-Kernels-Code/k-nucleotide/input.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)