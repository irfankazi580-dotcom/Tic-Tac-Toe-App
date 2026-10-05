import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

kivy.require('2.0.0')

class TicTacToeGame(BoxLayout):
    def __init__(self, **kwargs):
        super(TicTacToeGame, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        self.current_player = 'X'
        self.board = [''] * 9
        self.game_over = False

        # শিরোনাম এবং প্লেয়ারের টার্ন দেখানোর লেবেল
        self.status_label = Label(
            text="Tic-Tac-Toe\nPlayer X's Turn",
            font_size='24sp',
            size_hint=(1, 0.2),
            halign='center',
            valign='middle'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        self.add_widget(self.status_label)

        # ৩x৩ গ্রিড লেআউট (গেম বোর্ড)
        self.grid = GridLayout(cols=3, spacing=10, size_hint=(1, 0.6))
        self.buttons = []

        for i in range(9):
            btn = Button(
                text='',
                font_size='40sp',
                bold=True
            )
            btn.bind(on_press=lambda instance, index=i: self.on_btn_click(instance, index))
            self.buttons.append(btn)
            self.grid.add_widget(btn)

        self.add_widget(self.grid)

        # রিস্টার্ট বাটন
        self.restart_btn = Button(
            text="Restart Game",
            font_size='20sp',
            size_hint=(1, 0.15),
            background_color=(0.2, 0.6, 1, 1)
        )
        self.restart_btn.bind(on_press=self.reset_game)
        self.add_widget(self.restart_btn)

    def on_btn_click(self, instance, index):
        if self.board[index] == '' and not self.game_over:
            self.board[index] = self.current_player
            instance.text = self.current_player

            if self.check_winner(self.current_player):
                self.status_label.text = f"🎉 Player {self.current_player} Wins!"
                self.game_over = True
            elif '' not in self.board:
                self.status_label.text = "It's a Draw! 🤝"
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.text = f"Player {self.current_player}'s Turn"

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # অনুভূমিক (Rows)
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # উল্লম্ব (Columns)
            [0, 4, 8], [2, 4, 6]              # কোণাকুণি (Diagonals)
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def reset_game(self, instance):
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_over = False
        self.status_label.text = "Tic-Tac-Toe\nPlayer X's Turn"
        for btn in self.buttons:
            btn.text = ''

class TicTacToeApp(App):
    def build(self):
        self.title = "Tic-Tac-Toe Game"
        return TicTacToeGame()

if __name__ == '__main__':
    TicTacToeApp().run()
