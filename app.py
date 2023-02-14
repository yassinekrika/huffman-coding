import customtkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from NodeTree import NodeTree


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        # create the ui
        self.title("Huffman Coding")
        self.geometry("800x500")
        self.maxsize(800, 500)
        self.minsize(800, 500)
        self.config(bg="#17043d")

        font1 = ("Arial", 20)
        font2 = ("Arial", 15)
        font3 = ("Arial", 12)

        self.frame1 = customtkinter.CTkFrame(self, fg_color="#ffffff", width=430, height=480, corner_radius=20)
        self.frame1.place(x=350, y=25)

        self.label = customtkinter.CTkLabel(self, text="Add The String you want to Code :", font=font1, fg_color="#17043d")
        self.label.place(x=20, y=20)

        self.text_box = customtkinter.CTkTextbox(self, font=font2, text_color="#000000", fg_color="#ffffff", border_color="#ffffff", width=300, height=200)
        self.text_box.place(x=20, y=100)

        self.code_button = customtkinter.CTkButton(self, text="Code",font=font1, fg_color="#03a819", hover_color="#03a819", width=120, corner_radius=20, text_color="#ffffff", command = self.code)
        self.code_button.place(x=20, y=330)

        self.clear_button = customtkinter.CTkButton(self, text="Clear",font=font1, fg_color="#b86512", hover_color="#b86512", width=120, corner_radius=20, text_color="#ffffff", command = self.clear)
        self.clear_button.place(x=200, y=330)

        self.beforeCompression = customtkinter.CTkLabel(self, text="Before Compression : ", font=font1, fg_color="#17043d")
        self.beforeCompression.place(x=20, y=400)

        self.afterCompression = customtkinter.CTkLabel(self, text="After Compression : ", font=font1, fg_color="#17043d")
        self.afterCompression.place(x=20, y=430)

        self.compressionPercentage = customtkinter.CTkLabel(self, text="Compression percentage : ", font=font1, fg_color="#17043d")
        self.compressionPercentage.place(x=20, y=460)

        

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=font3, rowheight=50)
        style.configure("mystyle.Treeview.Heading", font=font3, background="white")
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        self.tv = ttk.Treeview(self.frame1, columns=(1,2,3), show="headings", style="mystyle.Treeview")

        self.tv.heading("1", text="Symbol")
        self.tv.column("1", width=150)

        self.tv.heading("2", text="Freq")
        self.tv.column("2", width=150)

        self.tv.heading("3", text="Coding")
        self.tv.column("3", width=150)

        self.tv.pack()

    def clear(self):
        self.text_box.delete("0.0", "end")
        self.beforeCompression.configure(text="Before Compression : ")
        self.afterCompression.configure(text="After Compression : ")   
        self.compressionPercentage.configure(text="Compression percentage : ")   
        self.tv.delete(*self.tv.get_children())

    def code(self):
            
            string = self.text_box.get("0.0", "end")
            
            if string == '\n' or string == "": 
                messagebox.showinfo("Error", "Please enter something") 
            
            else:
                # Main function implementing huffman coding
                def huffman_code_tree(node):
                    codes = {}

                    def traverse(node, code):
                        if type(node) is str:
                            codes[node] = code
                        else:
                            traverse(node.left, code + '0')
                            traverse(node.right, code + '1')

                    traverse(node, '')
                    return codes



                # Calculating frequency
                freq = {}
                for c in string:
                    if c in freq:
                        freq[c] += 1
                    else:
                        freq[c] = 1
                
                freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

                nodes = freq

                while len(nodes) > 1:
                    (key1, c1) = nodes[-1]
                    (key2, c2) = nodes[-2]
                    nodes = nodes[:-2]
                    node = NodeTree(key1, key2)
                    nodes.append((node, c1 + c2))

                    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
                    
                huffmanCode = huffman_code_tree(nodes[0][0])
                
                # calculate bits & percentages
                beforeCompressionValue = (len(self.text_box.get("0.0", "end")) - 1) * 8
                afterCompressionValue = 0  
                the_symbols = huffmanCode.keys()  

                for symbol in the_symbols:  
                    the_count = string.count(symbol)   
                    afterCompressionValue += the_count * len(huffmanCode[symbol])

                percentage = (afterCompressionValue * 100) / beforeCompressionValue
                
                # showing percentage to ui
                self.beforeCompression.configure(text=f"Before Compression : {beforeCompressionValue} bits")
                self.afterCompression.configure(text=f"After Compression : {afterCompressionValue} bits")
                self.compressionPercentage.configure(text=f"Compression percentage : {round(percentage, 2)}%")

                for (char, frequency) in freq:
                    if char != '\n':
                        self.tv.insert("", "end", values=(char, frequency, huffmanCode[char]))

if __name__=="__main__":
    app = App()
    app.mainloop()