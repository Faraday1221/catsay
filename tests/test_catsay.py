from pathlib import Path
from src.catsay.main import chat_bubble, _catsay

empty_bubble = " /  \\ \n|    |\n \\  / \n   V"
test_img = """
        _                        
        \`*-.                    
         )  _`-.                 
        .  : `. .                
        : _   '  \               
        ; *` _.   `*-._          
        `-.-'          `-.       
            ;       `       `.     
            :.       .        \    
            . \  .   :   .-'   .   
            '  `+.;  ;  '      :   
            :  '  |    ;       ;-. 
            ; '   : :`-:     _.`* ;
    [bug] .*' /  .*' ; .*`- +'  `*' 
        `*-*   `*-*  `*-*'        """


def test_empty_bubble():
    assert empty_bubble == chat_bubble("")


def test_catsay():
    img = _catsay(text="", reverse=False, filepath=Path(__file__).parent / "img/")
    t_img = empty_bubble + test_img
    assert t_img == img
