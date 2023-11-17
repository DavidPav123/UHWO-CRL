import subprocess

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/binary-trees/C/binarytreesC 21 ; } 2>> /workspaces/Rusty-Kernels-Code/binary-trees/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/binary-trees/C/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/binary-trees/C/binarytreesC 21", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/binary-trees/C++/binarytreesC++ 21 ; } 2>> /workspaces/Rusty-Kernels-Code/binary-trees/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/binary-trees/C++/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/binary-trees/C++/binarytreesC++ 21", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call("{ time /workspaces/Rusty-Kernels-Code/binary-trees/Rust/target/release/Rust 21 ; } 2>> /workspaces/Rusty-Kernels-Code/binary-trees/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(3):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/binary-trees/Rust/Results/massif{i}.txt\" /workspaces/Rusty-Kernels-Code/binary-trees/Rust/target/release/Rust 21", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)
