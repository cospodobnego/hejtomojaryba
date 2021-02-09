from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from random import randint
import ast


# handle default display view
class BaseView(View):
    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        return render(request, self.template_name, locals())


class Game2View(View):
    template_name = 'game.html'

    def get(self, request):

        board = [
            [randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3)],
            [randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3)],
            [randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3)],
            [randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3)],
            [randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3)],
            [randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3)],
            [randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3)],
            [randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3), randint(1, 3)],
        ]

        player_1_score = 0
        player_2_score = 0

        all_moves = "11,12,13,14,15,16,17,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,61,62,63,64,65,66,67,68,71,72,73,74,75,76,77,81,82,83,84,85,86,87,88"

        penguin1_a_possible_movements = all_moves
        penguin1_b_possible_movements = all_moves
        penguin1_c_possible_movements = all_moves
        penguin1_d_possible_movements = all_moves
        penguin2_a_possible_movements = all_moves
        penguin2_b_possible_movements = all_moves
        penguin2_c_possible_movements = all_moves
        penguin2_d_possible_movements = all_moves

        round_number = 0

        return render(request, self.template_name, locals())

    def post(self, request):
        round_number = int(request.POST.get('round_number'))
        round_number += 1

        position_penguin1_a = request.POST.get('penguin1_a')
        position_penguin1_b = request.POST.get('penguin1_b')
        position_penguin1_c = request.POST.get('penguin1_c')
        position_penguin1_d = request.POST.get('penguin1_d')

        position_penguin2_a = request.POST.get('penguin2_a')
        position_penguin2_b = request.POST.get('penguin2_b')
        position_penguin2_c = request.POST.get('penguin2_c')
        position_penguin2_d = request.POST.get('penguin2_d')

        # convert string into array
        board = ast.literal_eval(request.POST.get('board'))

        def update_data(player_name, position_penguin_a):
            # get penguin position
            x_a = int(list(position_penguin_a)[0]) - 1
            y_a = int(list(position_penguin_a)[1]) - 1

            # get score
            score = board[x_a][y_a]

            # update board with empty floe and penguin position
            board[x_a][y_a] = 0
            position_penguin_a = [int(x) for x in list(position_penguin_a)]

            return score, position_penguin_a

        if position_penguin1_a:
            player_1_score_a, position_penguin1_a = update_data('player_1', position_penguin1_a)
        else:
            player_1_score_a = 0

        if position_penguin1_b:
            player_1_score_b, position_penguin1_b = update_data('player_1', position_penguin1_b)
        else:
            player_1_score_b = 0

        if position_penguin1_c:
            player_1_score_c, position_penguin1_c = update_data('player_1', position_penguin1_c)
        else:
            player_1_score_c = 0

        if position_penguin1_d:
            player_1_score_d, position_penguin1_d = update_data('player_1', position_penguin1_d)
        else:
            player_1_score_d = 0

        if position_penguin2_a:
            player_2_score_a, position_penguin2_a = update_data('player_2', position_penguin2_a)
        else:
            player_2_score_a = 0

        if position_penguin2_b:
            player_2_score_b, position_penguin2_b = update_data('player_2', position_penguin2_b)
        else:
            player_2_score_b = 0

        if position_penguin2_c:
            player_2_score_c, position_penguin2_c = update_data('player_2', position_penguin2_c)
        else:
            player_2_score_c = 0

        if position_penguin2_d:
            player_2_score_d, position_penguin2_d = update_data('player_2', position_penguin2_d)
        else:
            player_2_score_d = 0

        def possible_movements(position_penguin1_a):

            # all board movements
            movements = []
            for i in range(8):
                for j in range(len(board[i])):
                    movements.append([i + 1, j + 1])

            # move right
            right = []
            for item in movements:
                if item[0] == position_penguin1_a[0] and item[1] > position_penguin1_a[1]:
                    if board[item[0]-1][item[1]-1] == 0:
                        break
                    else:
                        right.append(item)

            # move left
            temporarily_left = []
            for item in movements:
                if item[0] == position_penguin1_a[0] and item[1] < position_penguin1_a[1]:
                    temporarily_left.append(item)

            temporarily_left = list(sorted(temporarily_left, key=lambda x: x[1], reverse=True))
            left = []
            for item in temporarily_left:
                if board[item[0]-1][item[1]-1] == 0:
                    break
                else:
                    left.append(item)

            # move diagonal right down
            diagonal_right_down = []
            column = position_penguin1_a[1]
            for i in range(position_penguin1_a[0]+1, 9):
                if i % 2 == 0:
                    column += 1
                try:
                    if board[i-1][column-1] == 0:
                        break
                    else:
                        if column > 0:
                            diagonal_right_down.append([i, column])
                except:
                    pass

            # move diagonal right up
            diagonal_right_up = []
            column = position_penguin1_a[1]
            for i in range(position_penguin1_a[0]-1, 0, -1):
                if i % 2 != 0:
                    column -= 1
                try:
                    if board[i-1][column-1] == 0:
                        break
                    else:
                        if column > 0:
                            diagonal_right_up.append([i, column])
                except:
                    pass

            # move diagonal left down
            diagonal_left_down = []
            column = position_penguin1_a[1]
            for i in range(position_penguin1_a[0]+1, 9):
                if i % 2 != 0:
                    column -= 1
                try:
                    if board[i-1][column-1] == 0:
                        break
                    else:
                        if column > 0:
                            diagonal_left_down.append([i, column])
                except:
                    pass

            # move diagonal left up
            diagonal_left_up = []
            column = position_penguin1_a[1]
            for i in range(position_penguin1_a[0]-1, 0, -1):
                if i % 2 == 0:
                    column += 1
                try:
                    if board[i-1][column-1] == 0:
                        break
                    else:
                        if column > 0:
                            diagonal_left_up.append([i, column])
                except:
                    pass

            all_possible_movements = right + left + diagonal_right_down + diagonal_right_up + diagonal_left_down + diagonal_left_up
            all_possible_movements = ','.join([str(item[0]) + str(item[1]) for item in all_possible_movements])
            return all_possible_movements

        # all available starting movements
        available_movements = []
        for i in range(8):
            for j in range(len(board[i])):
                if board[i][j] != 0:
                    available_movements.append([i + 1, j + 1])

        penguin_all_movements = ','.join([str(item[0]) + str(item[1]) for item in available_movements])

        if position_penguin1_a:
            penguin1_a_possible_movements = possible_movements(position_penguin1_a)
        else:
            penguin1_a_possible_movements = penguin_all_movements

        if position_penguin1_b:
            penguin1_b_possible_movements = possible_movements(position_penguin1_b)
        else:
            penguin1_b_possible_movements = penguin_all_movements

        if position_penguin1_c:
            penguin1_c_possible_movements = possible_movements(position_penguin1_c)
        else:
            penguin1_c_possible_movements = penguin_all_movements

        if position_penguin1_d:
            penguin1_d_possible_movements = possible_movements(position_penguin1_d)
        else:
            penguin1_d_possible_movements = penguin_all_movements

        if position_penguin2_a:
            penguin2_a_possible_movements = possible_movements(position_penguin2_a)
        else:
            penguin2_a_possible_movements = penguin_all_movements

        if position_penguin2_b:
            penguin2_b_possible_movements = possible_movements(position_penguin2_b)
        else:
            penguin2_b_possible_movements = penguin_all_movements

        if position_penguin2_c:
            penguin2_c_possible_movements = possible_movements(position_penguin2_c)
        else:
            penguin2_c_possible_movements = penguin_all_movements

        if position_penguin2_d:
            penguin2_d_possible_movements = possible_movements(position_penguin2_d)
        else:
            penguin2_d_possible_movements = penguin_all_movements

        # update score
        player_1_score = request.POST.get('player_1')
        player_2_score = request.POST.get('player_2')

        if len(player_1_score) == 0:
            player_1_score = 0
        else:
            player_1_score = int(player_1_score)

        if len(player_2_score) == 0:
            player_2_score = 0
        else:
            player_2_score = int(player_2_score)

        player_1_score += sum([player_1_score_a, player_1_score_b, player_1_score_c, player_1_score_d])
        player_2_score += sum([player_2_score_a, player_2_score_b, player_2_score_c, player_2_score_d])

        # check no more moves condition
        game_finish_check = [penguin1_a_possible_movements, penguin1_b_possible_movements,
                             penguin1_c_possible_movements, penguin1_d_possible_movements,
                             penguin2_a_possible_movements, penguin2_b_possible_movements,
                             penguin2_c_possible_movements, penguin2_d_possible_movements]

        # check end game condition
        if all(value == 0 for row in board for value in row) or all(value == '' for row in game_finish_check for value in row):
            if player_1_score > player_2_score:
                messages.success(request, 'Game ended: Winner is Player 1')
            elif player_2_score > player_1_score:
                messages.success(request, 'Game ended: Winner is Player 2')
            else:
                messages.success(request, 'Game ended: Draw')

        return render(request, self.template_name, locals())
