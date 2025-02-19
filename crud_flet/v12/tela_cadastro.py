import flet as ft
import controle as con

def view():     
    return ft.View(
                "tela1",
                [                           
                    ft.Text('Tela 1', size=20)                    
                ],
                navigation_bar=con.barra_navegacao(),                    
            )
