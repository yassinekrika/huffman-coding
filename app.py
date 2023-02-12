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

        self.frame1 = customtkinter.CTkFrame(self, fg_color="#ffffff", width=450, height=500)
        self.frame1.place(x=350, y=0)

        self.label = customtkinter.CTkLabel(self, text="Add The String you want to Code :", font=font1, fg_color="#17043d")
        self.label.place(x=20, y=20)

        self.text_box = customtkinter.CTkTextbox(self, font=font2, text_color="#000000", fg_color="#ffffff", border_color="#ffffff", width=300, height=200)
        self.text_box.place(x=20, y=100)

        self.code_button = customtkinter.CTkButton(self, text="Code",font=font1, fg_color="#03a819", hover_color="#03a819", width=120, corner_radius=20, text_color="#ffffff", command = self.code)
        self.code_button.place(x=20, y=330)

        self.clear_button = customtkinter.CTkButton(self, text="Clear",font=font1, fg_color="#b86512", hover_color="#b86512", width=120, corner_radius=20, text_color="#ffffff", command = self.clear)
        self.clear_button.place(x=200, y=330)


        self.percentage_label = customtkinter.CTkLabel(self, text="Compresed precentage :", font=font1, fg_color="#17043d")
        self.percentage_label.place(x=20, y=370)

        self.percentage_value_label = customtkinter.CTkLabel(self, text="50%", font=font1, fg_color="#17043d")
        self.percentage_value_label.place(x=20, y=400)


    def clear(self):
            self.text_box.delete("0.0", "end")
            # change value of percentage
            self.percentage_value_label.configure(text="00%")

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

            print(' Char | Huffman code ')
            print('----------------------')
            for (char, frequency) in freq:
                print(' %-4r |%12s' % (char, huffmanCode[char]))



if __name__=="__main__":
    app = App()
    app.mainloop()