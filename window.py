import tkinter as tk



class AppWindow:
    def __init__(self, root, process_function):

        selected_row = None;

        def Msg_create():
            title = self.title.get("1.0", "end-1c");
            msg = self.text.get("1.0", "end-1c");
            process_function["create"](title, msg)

        def Msg_update():
            title = self.title.get("1.0", "end-1c");
            msg = self.text.get("1.0", "end-1c");
            process_function["update"](selected_row, title, msg)

        def Msg_delete():
            process_function["delete"](selected_row)

        def List_index(event):
            valgt_index_tuple = self.list.curselection()
    
            if valgt_index_tuple:
                index = valgt_index_tuple[0]
                selected_row = index;
                valgt_tekst = self.list.get(index)
                print(index, valgt_tekst)

        def Update_list(self):
            rows = process_function["read"]("");

            if rows:
                for row in rows:
                    self.list.insert(tk.END, row[3]);


        self.root = root;
        root.title("Text edit");
        root.geometry("400x300");

        self.root.rowconfigure(0, weight=1);
        self.root.rowconfigure(1, weight=1);
        self.root.rowconfigure(2, weight=8);
        self.root.columnconfigure(0, weight=3);
        self.root.minsize(400, 300);

        self.list = tk.Listbox(root)
        self.list.grid(row=2, column=1)

        self.list.bind("<<ListboxSelect>>", List_index)

        self.title = tk.Text(
            root,

        )
        self.text = tk.Text(
            root,
        )
        self.title.grid(row=1, column=0, sticky="w");
        self.text.grid(row=2, column=0, sticky="w");

        self.create = tk.Button(root, text="Create", command=Msg_create)
        self.read = tk.Button(root, text="Read", command=Msg_create)
        self.update = tk.Button(root, text="Update", command=Msg_update)
        self.delete = tk.Button(root, text="Delete", command=Msg_delete)

        self.create.grid(row=0, column=0, sticky="w", padx=0);
        self.read.grid(row=0, column=0, sticky="w", padx=30);
        self.update.grid(row=0, column=0, sticky="w", padx=60);
        self.delete.grid(row=0, column=0, sticky="w", padx=90);

        Update_list(self);


