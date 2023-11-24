import subprocess

for i in range(5):
    subprocess.call("time ((/workspaces/Rusty-Kernels-Code/reverse-complement/C/revcompC < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt) > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/reverse-complement/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/reverse-complement/C/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/reverse-complement/C/revcompC < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time ((/workspaces/Rusty-Kernels-Code/reverse-complement/C++/revcompC++ < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt) > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/reverse-complement/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/reverse-complement/C++/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/reverse-complement/C++/revcompC++ < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time ((/workspaces/Rusty-Kernels-Code/reverse-complement/Rust/target/release/Rust < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt) > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/reverse-complement/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/reverse-complement/Rust/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/reverse-complement/Rust/target/release/Rust < /workspaces/Rusty-Kernels-Code/reverse-complement/input.txt > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)




