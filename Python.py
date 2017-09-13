import pygame
from copy import deepcopy


class Python:
    __default_rect = pygame.Rect(0, 0, 10, 10)
    __head_pos = None
    __tail_segments = []
    # 0 is none, -1 is down/left, +1 is up/right
    __y_velocity = -1
    __x_velocity = 0
    __game_over = False

    def __init__(self, pos):
        self.__head_pos = pos
        for i in range(0, 4):
            segment = self.__default_rect.copy()
            segment.center = (pos[0], pos[1] + 20*i)
            self.__tail_segments.append(segment)

    def add_tail_segment(self):
        last_segment = self.__tail_segments[-1]
        second_last_segment = self.__tail_segments[-2]
        segment = self.__default_rect.copy()
        x, y = (0, 0)
        if last_segment.x == second_last_segment.x:
            x = last_segment.x
            if last_segment.y < second_last_segment.y:
                y = last_segment.y - 20
            else:
                y = last_segment.y + 20
        elif last_segment.y == second_last_segment.y:
            y = last_segment.y
            if last_segment.x < second_last_segment.x:
                x = last_segment.x - 20
            else:
                x = last_segment.x + 20
        segment.center = (x, y)
        self.__tail_segments.append(segment)

    def head_rect(self):
        head = self.__tail_segments[0].copy()
        return head

    def __segments_collide(self):
        for rect in self.__tail_segments:
            if len(rect.collidelistall(self.__tail_segments)) > 1 \
                    or not pygame.display.get_surface().get_rect().contains(rect):
                return True
        return False

    def __update_segments(self, new_head):
        last_segments = deepcopy(self.__tail_segments)
        self.__tail_segments[0].center = new_head
        self.__head_pos = new_head
        for i in range(1, len(last_segments)):
            self.__tail_segments[i].center = last_segments[i-1].center

    def move_python(self, key):
        if key == pygame.K_UP and self.__y_velocity != 1:
            self.__y_velocity = -1
            self.__x_velocity = 0
        elif key == pygame.K_DOWN and self.__y_velocity != -1:
            self.__y_velocity = 1
            self.__x_velocity = 0
        elif key == pygame.K_LEFT and self.__x_velocity != 1:
            self.__x_velocity = -1
            self.__y_velocity = 0
        elif key == pygame.K_RIGHT and self.__x_velocity != -1:
            self.__x_velocity = 1
            self.__y_velocity = 0

    def draw(self):
        if not self.__game_over:
            self.__update_segments((self.__head_pos[0] + 20*self.__x_velocity, self.__head_pos[1] + 20*self.__y_velocity))
            if self.__segments_collide():
                self.__game_over = True
            for segment in self.__tail_segments:
                pygame.draw.rect(pygame.display.get_surface(), (34, 139, 34), segment)
            return True
        else:
            return False
