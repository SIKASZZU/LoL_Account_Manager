import customtkinter as ctk
from tkinter import messagebox

def on_button_click(root, account_details):
    global account_selected
    account_selected = account_details
    root.destroy()

def toggle_input_fields(new_account_frame):
    if new_account_frame.winfo_ismapped():
        new_account_frame.pack_forget()
    else:
        new_account_frame.pack(pady=10)

def activate_window(accounts_list):
    acc_details = {account[0]: (account[1], account[2]) for account in accounts_list}
    
    root = ctk.CTk()
    root.title("Account Manager")
    root.geometry("400x500")
    root.configure(bg="#1e1e1e")

    new_account_button = ctk.CTkButton(root, text="NEW ACCOUNT", command=lambda: toggle_input_fields(new_account_frame), fg_color="#4CAF50", text_color="black", font=("Arial", 18, "bold"))
    new_account_button.pack(pady=10)

    frame = ctk.CTkFrame(root, fg_color="#1e1e1e", corner_radius=8)
    frame.pack(pady=10, padx=10, fill='x')
    
    for key in acc_details.keys():
        account_details = acc_details[key]
        button = ctk.CTkButton(frame, text=key, command=lambda key=key: on_button_click(root, account_details), fg_color="#333333", hover_color="#666666")
        button.pack(pady=5, fill='x', padx=5)
    
    
    new_account_frame = ctk.CTkFrame(root, fg_color="#222222", corner_radius=8)
    
    entry_name = ctk.CTkEntry(new_account_frame, placeholder_text="Enter name", width=240)
    entry_name.pack(pady=15, padx=10, fill='x')
    
    entry_acc = ctk.CTkEntry(new_account_frame, placeholder_text="Enter login in detail: account name", width=240)
    entry_acc.pack(pady=15, padx=10, fill='x')
    
    entry_pass = ctk.CTkEntry(new_account_frame, placeholder_text="Enter login in detail: account password", show="*", width=240)
    entry_pass.pack(pady=5, padx=10, fill='x')
    
    def add_account():
        username = entry_name.get().strip()
        acc_name = entry_acc.get().strip()
        password = entry_pass.get().strip()
        
        if not username or not acc_name or not password:
            messagebox.showerror("Error", "All fields must be filled.")
            return
        
        if username in acc_details:
            messagebox.showerror("Error", "Username already exists.")
            return
        
        accounts_list.append((username, acc_name, password))
        acc_details[username] = (acc_name, password)
        
        with open("acc_details.txt", "a") as f:
            f.write(f"{username}, {acc_name}, {password}\n")
        
        ctk.CTkButton(frame, text=username, command=lambda: on_button_click(root, (acc_name, password)), fg_color="#888888", hover_color="#666666").pack(pady=5, fill='x', padx=5)
        entry_name.delete(0, 'end')
        entry_acc.delete(0, 'end')
        entry_pass.delete(0, 'end')
        toggle_input_fields(new_account_frame)
    
    submit_button = ctk.CTkButton(new_account_frame, text="Add Account", command=add_account, fg_color="#4CAF50", text_color="white")
    submit_button.pack(pady=10)
    
    root.mainloop()
    return account_selected
