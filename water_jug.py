import math
import copy

class Node:
    def __init__(self,x,y):    
        self.x = x
        self.y = y

def main():
    max_x = 4
    max_y = 3
    visited = [[0 for i in range(max_y+1)] for i in range(max_x+1)]
    # print(visited)
    node = Node(0,0)
    stack = []
    count = 0
    t_node = Node(0,0)
    while True:
        print("test : ( "+str(node.x)+", "+str(node.y)+" )",end="  ")
        count += 1
        visited[node.x][node.y] = 1
        # print(visited[0][0])
        if(node.x == 2 or node.y == 2):
            node.x = 2
            node.y = 0
            print("Goal State reached")
        if(node.x < 4 and visited[4][node.y] == 0):
            temp = node.x
            node.x = 4
            t_node = copy.copy(node)
            print("( "+str(t_node.x)+", "+str(t_node.y)+" )",end="  ")
            stack.append(t_node)
            visited[t_node.x][t_node.y] = 1
            # print("( "+str(stack[0].x)+", "+str(stack[0].y)+" )",end="  ")
            node.x = temp
        if(node.y < 3 and visited[node.x][3] == 0):
            # print("test : ( "+str(node.x)+", "+str(node.y)+" )",end="  ")
            temp = node.y
            node.y = 3
            t_node = copy.copy(node)
            print("( "+str(t_node.x)+", "+str(t_node.y)+" )",end="  ")
            stack.append(t_node)
            visited[t_node.x][t_node.y] = 1
            # print("( "+str(stack[1].x)+", "+str(stack[1].y)+" )",end="  ")
            node.y = temp
        if(node.x>0 and visited[0][node.y] == 0):
            temp = node.x
            node.x = 0
            t_node = copy.copy(node)
            print("( "+str(node.x)+", "+str(node.y)+" )",end="  ")
            stack.append(t_node)
            visited[t_node.x][t_node.y] = 1
            node.x = temp
        if(node.y>0 and visited[node.y][0] == 0):
            temp = node.y
            node.y = 0
            t_node = copy.copy(node)
            print("( "+str(node.x)+", "+str(node.y)+" )",end="  ")
            stack.append(t_node)
            visited[t_node.x][t_node.y] = 1
            node.y = temp
        if(node.y>0 and node.x+node.y>0 and node.x+node.y >= 4 and visited[4][node.y-(4-node.x)] == 0):
            temp = node.x
            temp_1 = node.y
            node.x = 4
            node.y = node.y-(4-node.x)
            t_node = copy.copy(node)
            print("( "+str(node.x)+", "+str(node.y)+" )",end="  ")
            stack.append(t_node)
            visited[t_node.x][t_node.y] = 1
            # node.x = temp
            # node.y = temp_1
        if(node.x>0 and node.x+node.y>0 and node.x+node.y >= 3 and visited[node.x-(3-node.y)][3] == 0):
            temp = node.x
            temp_1 = node.y
            node.x = node.x-(3-node.y)
            node.y = 3
            t_node = copy.copy(node)
            print("( "+str(node.x)+", "+str(node.y)+" )",end="  ")
            stack.append(t_node)
            visited[t_node.x][t_node.y] = 1
            node.x = temp
            node.y = temp_1
        if(node.y>=0 and node.x+node.y>0 and node.x+node.y <= 4 and visited[node.x+node.y][0] == 0):
            temp = node.x
            temp_1 = node.y
            node.x = node.x+node.y
            node.y = 0
            t_node = copy.copy(node)
            print("( "+str(node.x)+", "+str(node.y)+" )",end="  ")
            stack.append(t_node)
            visited[node.x][node.y] = 1
            node.x = temp
            node.y = temp_1
        if(node.x>=0 and node.x+node.y>0 and node.x+node.y <= 3 and visited[0][node.x+node.y] == 0):
            temp = node.x
            temp_1 = node.y
            node.x = 0
            node.y = node.x+node.y
            t_node = copy.copy(node)
            print("( "+str(node.x)+", "+str(node.y)+" )")
            stack.append(t_node)
            visited[node.x][node.y] = 1
            node.x = temp
            node.y = temp_1
        # for i in stack:
        #     print(i.x,i.y,end=" ")
        if((len(stack) == 0)):
            break
        node = stack.pop()
        print()
        # break
        # print("end test : ( "+str(node.x)+", "+str(node.y)+" )")
        # if(node.x <= 4 and node.y > 0 and visited[node.x])

if __name__ == "__main__":
    main()
