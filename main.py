# Integration Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from sympy import Limit, Symbol, S, diff, integrate, solve
import math

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "KSquared-Mathematics :"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 

        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "Integration Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"                 
                
""")

#Menu
Builder.load_string("""
<Menu>:
    id: Menu
    name: "Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
                    
            Button:
                font_size: '20sp'
                background_color: 0, 1, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Integration Calculator"
                on_release:
                    app.root.current = "Integration"
                    root.manager.transition.direction = "left"
                    
            Button:
                font_size: '20sp'
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Button:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.ksquaredmathematics.com/subscribe') 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 800
                width: 800
                
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '15sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-Mathematics?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: '15sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Integration Calculator v0.1"
                
            Label:
                font_size: '15sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
""")

#Integration Calculator
Builder.load_string("""
<Integration>
    id:Integration
    name:"Integration"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Integration Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        prime.text = ""
                        respect.text = ""
                        value.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "f(x)="
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 125
                padding: 10              
            
            TextInput:
                id: prime
                text: prime.text
                hint_text: "# of times to integrate"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 125
                padding: 10              
                input_filter: lambda text, from_undo: text[:2 - len(prime.text)]
                
            TextInput:
                id: respect
                text: respect.text
                hint_text: "With respect to: x, y or z"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 125
                padding: 10  
                input_filter: lambda text, from_undo: text[:1 - len(respect.text)]
                
            TextInput:
                id: value
                text: value.text
                hint_text: "Definite Integral: a,b"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 125
                padding: 10  
                
                    
            Button:
                id: steps
                text: "Integrate"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1, 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets()
                    Integration.Integrate(entry.text + "&" + prime.text + "$" + respect.text + "%" + value.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Integration(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Integration, self).__init__(**kwargs)

    layouts = []
    def Integrate(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("~~~~~~~~~~~~~~~~~~~~")
        print("INTEGRATE")
        
        try:
            print("Entry",entry)
            amp = entry.find("&")
            dollar = entry.find("$")
            percent_sign = entry.find("%")
            
            func = entry[:amp]
            print("func",func)       
            
            prime = entry[amp+1:dollar]
            print("Prime:",prime)
            if prime == "":
                prime = 0
            
            respect = entry[dollar + 1:percent_sign]
            print("respect:",respect)
            
            value = entry[percent_sign+1:]
            print("value:",value)
            if value == "":
                value = "Nothing"
            if value.count(",") == 1:
                comma = value.find(",")
                a = value[:comma]
                print("a = ",a)
                
                b = value[comma+1:]
                print("b = ",b)
            
            x = Symbol("x")
            y = Symbol("y")
            z = Symbol("z")
            
            if int(prime) > 0 and str(respect) != "":
                self.ids.list_of_steps.add_widget(Label(text= "f(" + respect + ") = " + str(func).replace("**","^").replace("*x","x").replace("*y","y").replace("*z","z").replace("-"," - ").replace("+"," + ").replace("***","**") ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Integrate " + str(prime) + " time(s) with respect to " + str(respect),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                print("_________________________________________")
                
                func = func.replace(" ","").replace("+"," + ").replace("-"," - ").replace("^ -","^-").replace("^ +","^+")
                print("func",func)
                
                k = 0
                while k < int(prime):
                    if func.count("(") > 0 and func.count(")") > 0:
                        if func.count("(") == func.count(")"):
                            print("Parenthesis Found")
                            i = 0
                            while i < len(func):
                                if func[i] == ")":
                                    right_par_index = i
                                    print("right_par_index",right_par_index)
                                    left_par_index = func[:i].rfind("(")
                                    print("left_par_index",left_par_index)
                                    range_pars = func[left_par_index:right_par_index+1]
                                    print(range_pars)
                                    cleaned = range_pars.replace(" ","")
                                    print("cleaned",cleaned)
                                    func = func[:left_par_index] + cleaned + func[right_par_index+1:] 
                                    print("func cleaned",func)
                                    print()
                                i = i + 1 
                                
                        else:
                            print("Parentheses Unbalanced!")
                    
                    func_list = func.strip().split(" ")
                    print()
                    print("func_list",func_list)
                    print()
                    
                    #If + or - is first element in list
                    new_func_list = []
                    if func_list[0] == "+" or func_list[0] == "-":
                        print("IF")
                        i = 0
                        while i < len(func_list):
                            if func_list[i] == "+" or func_list[i] == "-":
                                new_func_list.append(func_list[i] + func_list[i+1])
                            i = i + 1
                        print("new_func_list",new_func_list)
                    #If + or - is second element in list    
                    elif len(func_list) > 1:
                        if func_list[1] == "+" or func_list[1] == "-":
                           print("ELIF")
                           i = 0
                           while i < len(func_list):
                               if func_list[i] == "+" or func_list[i] == "-":
                                   new_func_list.append(func_list[i] + func_list[i+1])
                               i = i + 1
                           print("new_func_list:",new_func_list)
                           new_func_list = [func_list[0]] + new_func_list
                           print("new_func_list",new_func_list)
                        
                    #If + or - is not apart of list
                    else:
                        print("ELSE")
                        new_func_list.append(func_list[0])
                        print("new_func_list",new_func_list)
                        
                    print()
                    print("integrate each element and store in empty list")
                    print()
                    
                    i = 0
                    while i < len(new_func_list):
                        #finding e
                        if new_func_list[i].count("e") > 0 and new_func_list[i].count("s") == 0 and new_func_list[i].count("c") == 0 and new_func_list[i].count("t") == 0:
                            print()
                            print("Found e")
                            carrot_index = new_func_list[i].find("^")
                            print("carrot_index: ",carrot_index)
                            exponent_range = new_func_list[i][carrot_index+1:]
                            print("exponent_range:",exponent_range)
                            if exponent_range[0] == "x" or exponent_range[0] == "y" or exponent_range[0] == "z":
                                exponent_range = "1" + exponent_range
                                print("e^x fixed: ",exponent_range)
                                new_func_list[i] = new_func_list[i][:carrot_index] + "^" + exponent_range
                                print("new_func_list[i]:",new_func_list[i])
                                if new_func_list[i][0] == "*":
                                    new_func_list[i] = new_func_list[i][1:]
                                    print("found stray *")
                                    print("Cleaned:",new_func_list[i])
                            else:
                                print("e element okay for integration: ",new_func_list[i])
                                if new_func_list[i][0] == "*":
                                    new_func_list[i] = new_func_list[i][1:]
                                    print("found stray *")
                                    print("Cleaned:",new_func_list[i])
                        #finding all other elements
                        else:
                            print()
                            print("Found non-e element:",new_func_list[i])
                            if new_func_list[i][0] == "*":
                                new_func_list[i] = new_func_list[i][1:]
                                print("found stray *")
                                print("Cleaned:",new_func_list[i])
                            
                        i = i + 1
                        
                    print()
                    print("new_func_list with fixed e elements: ",new_func_list)
                    print()
                    
                    answer_integrated = []
                    #While loop to clean each element
                    i = 0
                    while i < len(new_func_list):
                        print("Cleaning ",new_func_list[i])
                        new_func_list[i] = new_func_list[i].replace("^","**").replace("x","*x").replace("y","*y").replace("z","*z")
                        new_func_list[i] = new_func_list[i].replace("sin","*sin").replace("cos","*cos").replace("tan","*tan").replace("sec","*sec").replace("csc","*csc").replace("cot","*cot")
                        new_func_list[i] = new_func_list[i].replace("e**","*e**").replace("(*e**","(e**").replace("-*","-").replace("+*","+").replace("(*x","(x").replace("(*y","(y").replace("(*z","(z")
                        print("new_func_list[i]: ",new_func_list[i])
                        
                        if new_func_list[i][0] == "*":
                            new_func_list[i] = new_func_list[i][1:]
                            print("found stray *")
                            print("Cleaned:",new_func_list[i])
                        
                        print()
                        i = i + 1
                        
                    print()
                    print("new_func_list with cleaned elements: ",new_func_list)
                    print()
                        
                    #Concat all cleaned elements and integrate
                    #OR while loop to integrate each element and then concat
                    
                    func_concat = str(new_func_list).replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","").replace("+"," + ").replace("-"," - ")
                    print("func_concat: ",func_concat)
                    print()
                    if respect == "x":
                        print("Integrating with respect to X")
                        func_integrated = str(integrate(str(func_concat),x)).replace("**","^")
                        print("func_integrated",func_integrated)
                    elif respect == "y":
                        print("Integrating with respect to Y")
                        func_integrated = str(integrate(str(func_concat),y)).replace("**","^")
                        print("func_integrated",func_integrated)
                    elif respect == "z":
                        print("Integrating with respect to Z")
                        func_integrated = str(integrate(str(func_concat),z)).replace("**","^")
                        print("func_integrated",func_integrated)
                    
                    func_integrated_list = func_integrated.split(" ")
                    print("func_integrated_list",func_integrated_list)
                    
                    func_integrated_list_empty = []
                    j = 0
                    while j < len(func_integrated_list):
                        if func_integrated_list != "+" or func_integrated_list != "-":
                            print("found non +-")
                            if func_integrated_list[j].count("/") > 0:
                                print("if")
                                div_sign_index = func_integrated_list[j].find("/")
                                print("div_sign_index",div_sign_index)
                                func_integrated_list_to_append = "(" + func_integrated_list[j][:div_sign_index] + ")" + func_integrated_list[j][div_sign_index:]
                                print("func_integrated_list_to_append",func_integrated_list_to_append)
                                func_integrated_list_empty.append(func_integrated_list_to_append)
                            else:
                                print("else")
                                func_integrated_list_empty.append(func_integrated_list[j])
                        else:
                            func_integrated_list_empty.append(func_integrated_list[j])
                        j = j + 1
                    print("func_integrated_list_empty",func_integrated_list_empty)
                        
                            
                    if len(func_integrated_list_empty) > 5:
                        func_integrated_list_empty_to_five = str(func_integrated_list_empty[:5]).replace("[","").replace("]","").replace(",","").replace("'","")
                        print("func_integrated_list_empty_to_five",func_integrated_list_empty_to_five)
                        
                        func_integrated_list_empty_five_out = str(func_integrated_list_empty[5:]).replace("[","").replace("]","").replace(",","").replace("'","")
                        print("func_integrated_list_empty_five_out",func_integrated_list_empty_five_out)
                    
                        self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "∫" * (k+1) + "f" + "(" + respect + ") = " + func_integrated_list_empty_to_five,font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= func_integrated_list_empty_five_out,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                    else:
                        func_integrated_list_empty = str(func_integrated_list_empty[:]).replace("[","").replace("]","").replace(",","").replace("'","")
                        self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= "∫" * (k+1) + "f" + "(" + respect + ") = " + func_integrated_list_empty,font_size = '15sp', size_hint_y= None, height=100))

                    
                    func = func_integrated.replace("**","^").replace("*","")
                    print("func ready for next loop, func = ",func_integrated)
                    print()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    k = k + 1
                    
            if value != "Nothing":
                print("func = ",func_integrated)
                
                func_a = str(func_integrated).replace(respect,a).replace("sqrt","*math.sqrt").replace("pi","*math.pi").replace("^","**").replace("sin","*math.sin").replace("cos","*math.cos").replace("tan","*math.tan").replace("csc","*math.csc").replace("sec","*math.sec").replace("cot","*math.cot").replace("log","*math.log").replace("e","*math.e").replace("smath.ec","*math.sec").replace("math.smath.secc","*math.sec").replace("-*","-").replace(" *m"," m").replace("(*m","(m")
                print("func_a replaced respect = ",func_a)
                
                if func_a[:2] == "*m":
                    func_a = func_a[1:]
                    print("func_a cleaned front",func_a)
                
                func_a_evaled = eval(str(func_a))
                print("func_a_evaled = ",func_a_evaled)
                
                self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "∫f" + "(" + a + ") = " + "{:,.2f}".format(float(str(func_a_evaled))),font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                func_b = str(func_integrated).replace(respect,b).replace("sqrt","*math.sqrt").replace("pi","*math.pi").replace("^","**").replace("sin","*math.sin").replace("cos","*math.cos").replace("tan","*math.tan").replace("csc","*math.csc").replace("sec","*math.sec").replace("cot","*math.cot").replace("log","*math.log").replace("e","*math.e").replace("smath.ec","*math.sec").replace("math.smath.secc","*math.sec").replace("-*","-").replace(" *m"," m").replace("(*m","(m")
                print("func_b replaced respect = ",func_b)
                
                if func_b[:2] == "*m":
                    func_b = func_b[1:]
                    print("func_b cleaned front",func_b)
                
                func_b_evaled = eval(str(func_b))
                print("func_b_evaled = ",func_b_evaled)

                self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "∫f" + "(" + b + ") = " + "{:,.2f}".format(float(str(func_b_evaled))),font_size = '15sp', size_hint_y= None, height=100))
                
                a = str(eval(a.replace("sqrt","math.sqrt").replace("pi","math.pi").replace("ln","math.log").replace("log","math.log").replace("e","math.e").replace("^","**")))
                    
                b = str(eval(b.replace("sqrt","math.sqrt").replace("pi","math.pi").replace("ln","math.log").replace("log","math.log").replace("e","math.e").replace("^","**")))
                
                print("a = ",a)
                print("b = ",b)
                
                if float(a) < float(b):
                    self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "∫f" + "(" + b + ") - " + "∫f" + "(" + a + ") =",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "{:,.2f}".format(float(str(func_b_evaled))) + " - " + "{:,.2f}".format(float(str(func_a_evaled))) + " =",font_size = '15sp', size_hint_y= None, height=100))
                    
                    integral_evaled = str(float(func_b_evaled) - float(func_a_evaled))
                    print("integral_evaled",integral_evaled)
 
                    self.ids.list_of_steps.add_widget(Label(text= "{:,.2f}".format(float(integral_evaled)),font_size = '15sp', size_hint_y= None, height=100))
                 
                else:
                    self.ids.list_of_steps.add_widget(Label(text= "-----------------------------------------------------------------------------------------------" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "b must be greater than a!" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
            else:
                if int(prime) == 0:
                    self.ids.list_of_steps.add_widget(Label(text= "Prime must be greater than 0!" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif respect == "":
                    self.ids.list_of_steps.add_widget(Label(text= "Respect must be entered" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)        
            
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass            

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(Integration(name="Integration"))
sm.add_widget(updates(name="updates"))
sm.current = "Homepage"   

class Integration(App):
    def __init__(self, **kwargs):
        super(Integration, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    Integration().run()
