import socket
import tkinter as tk
from tkinter import messagebox, scrolledtext

def port_scanner(target_ip, start_port, end_port):
    open_ports = []
    results_text.delete(1.0, tk.END)
    results_text.insert(tk.END, f"Scanning {target_ip} for open ports from {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
            results_text.insert(tk.END, f"[+] Port {port} is open\n")
        
        sock.close()
    
    if not open_ports:
        results_text.insert(tk.END, "No open ports found.\n")
    else:
        results_text.insert(tk.END, f"Open ports: {open_ports}\n")

def start_scan():
    target_ip = ip_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid port numbers (1-65535) and ensure start port is less than or equal to end port.")
        return

    port_scanner(target_ip, start_port, end_port)

# GUI Setup
root = tk.Tk()
root.title("Port Scanner")

# IP Address Entry
tk.Label(root, text="Target IP Address:").grid(row=0, column=0, padx=5, pady=5)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

# Port Range Entry
tk.Label(root, text="Start Port:").grid(row=1, column=0, padx=5, pady=5)
start_port_entry = tk.Entry(root)
start_port_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="End Port:").grid(row=2, column=0, padx=5, pady=5)
end_port_entry = tk.Entry(root)
end_port_entry.grid(row=2, column=1, padx=5, pady=5)

# Scan Button
scan_button = tk.Button(root, text="Start Scan", command=start_scan)
scan_button.grid(row=3, column=0, columnspan=2, pady=10)

# Results Display
results_text = scrolledtext.ScrolledText(root, width=50, height=15)
results_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
