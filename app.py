import customtkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from NodeTree import NodeTree
# create the ui


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

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

        tv = ttk.Treeview(self.frame1, columns=(1,2,3), show="headings", style="mystyle.Treeview")
        tv.heading("1", text="Symbol")
        tv.column("1", width=150)

        tv.heading("2", text="Freq")
        tv.column("2", width=150)

        tv.heading("3", text="Coding")
        tv.column("3", width=150)
        
        

        tv.pack()

    def clear(self):
        self.text_box.delete("0.0", "end")
        self.beforeCompression.configure(text="Before Compression : ")
        self.afterCompression.configure(text="After Compression : ")   
        self.compressionPercentage.configure(text="Compression percentage : ")   

    def code(self):
            # print('its working')

            # string = 'BCAADDDCCACACACCC'
            string = self.text_box.get("0.0", "end")

            # Main function implementing huffman coding
            def huffman_code_tree(node, left=True, binString=''):
                if type(node) is str:
                    return {node: binString}
                (l, r) = node.children()
                d = dict()
                d.update(huffman_code_tree(l, True, binString + '0'))
                d.update(huffman_code_tree(r, False, binString + '1'))
                return d


            # Calculating frequency
            freq = {}
            for c in string:
                if c in freq:
                    freq[c] += 1
                else:
                    freq[c] = 1
            dicFreq = freq
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
            print(huffmanCode)

            print(' Char | Huffman code ')
            print('----------------------')
            for (char, frequency) in freq:
                print(' %-4r |%12s' % (char, huffmanCode[char]))

            
            # calculate bits & percentages

            beforeCompressionValue = (len(self.text_box.get("0.0", "end")) - 1) * 8
            afterCompressionValue = 0  
            the_symbols = huffmanCode.keys()  

            for symbol in the_symbols:  
                the_count = string.count(symbol)  
                # calculating how many bit is required for that symbol in total  
                afterCompressionValue += the_count * len(huffmanCode[symbol])

            percentage = (afterCompressionValue * 100) / beforeCompressionValue

            self.beforeCompression.configure(text=f"Before Compression : {beforeCompressionValue} bits")
            self.afterCompression.configure(text=f"After Compression : {afterCompressionValue} bits")
            self.compressionPercentage.configure(text=f"Compression percentage : {round(percentage, 2)}%")

            # insert value into the table 
            # self.tv.delete(*self.tv.get_children())
            # for str in huffmanCode:
            # self.tv.insert("", "end", values=("hey", "hh", 12))
            # self.tv.insert("", "end", values=("hey", "hh", 12))

if __name__=="__main__":
    app = App()
    app.mainloop()