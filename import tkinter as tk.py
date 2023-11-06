import tkinter as tk

def convert_cfg_to_lmd_logic(cfg, start_symbol):
    def derive_lmd(cfg_dict, current_symbol):
        if current_symbol in cfg_dict:
            production = cfg_dict[current_symbol][0]  
            lmd_result = [current_symbol]
            for symbol in production.split():
                lmd_result.append('=>')
                lmd_result.append(derive_lmd(cfg_dict, symbol))
            return ' '.join(lmd_result)
        else:
            return current_symbol
    
    # Split the CFG text into production rules
    production_rules = [rule.strip() for rule in cfg.split('\n') if rule.strip()]
    
    # Create a dictionary to represent the production rules
    cfg_dict = {}
    for rule in production_rules:
        left, right = rule.split('->')
        cfg_dict[left.strip()] = [prod.strip() for prod in right.split('|')]
    
    lmd_result = derive_lmd(cfg_dict, start_symbol)
    return lmd_result

def convert_cfg_to_lmd():
    cfg = cfg_text.get("1.0", "end-1c")  # Get the CFG from the text widget
    start_symbol = start_symbol_entry.get()

    # Implement the CFG to LMD conversion logic here
    lmd_result = convert_cfg_to_lmd_logic(cfg, start_symbol)

    # Display the LMD result in the output text widget
    lmd_text.delete("1.0", "end")
    lmd_text.insert("1.0", lmd_result)

# Create the main application window
app = tk.Tk()
app.title("CFG to LMD Converter")

# Create and place GUI elements
cfg_label = tk.Label(app, text="Enter CFG:")
cfg_label.pack()

cfg_text = tk.Text(app, height=5, width=40)
cfg_text.pack()

start_symbol_label = tk.Label(app, text="Start Symbol:")
start_symbol_label.pack()

start_symbol_entry = tk.Entry(app)
start_symbol_entry.pack()

convert_button = tk.Button(app, text="Convert", command=convert_cfg_to_lmd)
convert_button.pack()

lmd_label = tk.Label(app, text="LMD Result:")
lmd_label.pack()

lmd_text = tk.Text(app, height=5, width=40)
lmd_text.pack()

# Start the GUI event loop
app.mainloop()
