# half of its code is stolen from stackoverflow and CodePulse pls sub to him hes cool
# rest is spaggetti code written by me :D
# unofficial name: TROLLCODE
# wanna make like a mixture of basic and LOLCODE

# constants (no 1 million hashtags becuause its 3 lines)
DIGITS = '0123456789'





###############################
# tokens and stuff
###############################



# tt stands for token type
TT_INT       = 'TT_INT' # intiger
TT_FLOAT     = 'TT_FLOAT' # float
TT_PLUS      = 'TT_PLUS'   # plus
TT_MINUS     = 'TT_MINUS'  # minus
TT_MUL       = 'TT_MUL' # multiply 
TT_DIV       = 'TT_DIV' # divide
TT_LPAREN    = 'TT_LPAREN' # left parenthesis or however they're spelled
TT_RPAREN    = 'TT_RPAREN' # right parenthesis or however they're spelled



class Token:

    def __init__(self, type_. value):
        self.type = type_
        self.value = value


    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'



###############################
# Lexer (ooooooooooooo)
###############################





class Bug: # (the error bug, not the insect bug)
     def __init__(self, bug_name, details):
         self.bug_name = bug_name
         self.details = details


    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result     
      


class IllegalCharBug(Bug):
    def __init__(self, details):
        super().__init__('OMG ILLEGAL CHAR ERROR!111!1 TROLLFACE', details)     # im good at naming things
class Lexer:


    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()


    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos]  if self.pos < len(self.text else None)    




    def make_tokens(self):


        tokens = []     


        # copy pasting is fun
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()

            elif self.current_char in DIGITS:
                tokens.append(self.make_number)   

            elif self.current_char in '+':
                tokens.append(Token(TT_PLUS)) 
                self.advance()

            elif self.current_char in '-':
                tokens.append(Token(TT_MINUS)) 
                self.advance()    

            elif self.current_char in '*':
                tokens.append(Token(TT_MUL)) 
                self.advance()        

            elif self.current_char in '/':
                tokens.append(Token(TT_DIV)) 
                self.advance()       

            elif self.current_char in '(':
                tokens.append(Token(TT_LPAREN)) 
                self.advance()        

            elif self.current_char in ')':
                tokens.append(Token(TT_RPAREN)) 
                self.advance()  

            else:
                #error              



        return tokens




    def make_number(self):
        num_str = ''    
        dot_count = 0 

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.' 
            else:
                num_str += self.current_char

        if dot_count == 0:
            return Token (TT_INT, int(num_str))     
        else:
            return Token(TT_FLOAT, float(num_str))      






