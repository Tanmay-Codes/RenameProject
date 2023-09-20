from tkinter import *
import os
from tkinter import messagebox
from datetime import datetime


def call():
    path = path_entry.get()
    search = search_entry.get()
    replace = rename_entry.get()
    date = date_entry.get()
    old_name = []
    replaced_name = []
    if date == "":
        is_ok = messagebox.askokcancel(title="Date not entered", message="Do you want to add today's date?")
        if is_ok:
            now = datetime.now()
            date = now.strftime(f"_%y%m%d")

    os.chdir(path)
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        old_name.append(f_name)
        old_name_path = fr"{path}\{f_name}{f_ext}"
        new_name = f_name.replace(search, replace)
        rn = new_name + date
        replaced_name.append(rn)
        new_name_path = fr"{path}\{new_name}{date}{f_ext}"
        os.rename(old_name_path, new_name_path)

    def restore():
        for i in range(len(old_name)):
            old_name_path_restore = fr"{path}\{replaced_name[i]}{f_ext}"
            new_name_path_restore = fr"{path}\{old_name[i]}{f_ext}"
            os.rename(old_name_path_restore, new_name_path_restore)

    restore_btn = Button(text="Restore", command=restore)
    restore_btn.grid(row=3, column=2)


# UI for the rename files

window = Tk()
window.title("File Renaming system")

window.config(height=400, width=400)
window.config(padx=100, pady=100)

# The OS path entry
path_entry_label = Label(text="File Path: ")
path_entry_label.grid(row=0, column=0)
path_entry = Entry(width=30)
path_entry.grid(row=0, column=1)

# The search entry box
search_entry_label = Label(text="Search for: ")
search_entry_label.grid(row=1, column=0)
search_entry = Entry(width=20)
search_entry.grid(row=1, column=1)

# The rename entry box
replace_label = Label(text="Replace by:")
replace_label.grid(row=2, column=0)
rename_entry = Entry(width=20)
rename_entry.grid(row=2, column=1)

# The rename button
replace_btn = Button(text="Replace", command=call)
replace_btn.grid(row=3, column=1)

date_label = Label(text="Date:")
date_label.grid(row=0, column=2)
date_entry = Entry(width=20)
date_entry.grid(row=0, column=3)

window.mainloop()
