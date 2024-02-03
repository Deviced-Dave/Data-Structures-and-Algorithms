class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        pass


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')


a.next = b
b.next = c
c.next = d


# A -> B -> C -> D -> None

# def print_list(head):                     # Traversal Algo
#     current = head
#     while current is not None:
#         print(current.val)
#         current = current.next

# def print_list(head):                     # Traversal Algo
    
#     if head is None:
#         return
    
#     print(head.val)
#     print_list(head.next)


## print_list(a)


# def append_in_list(head):                   # Returns list of node values   
#     current = head
#     values = []
    
#     while current != None:
#         values.append(current.head)
#         current = current.next

#     return values

## append_in_list(a)


# def sum_list(head):                         # Returns sum of all node values
#     current = head
#     sum = 0

#     while current != None:
#         sum = sum + current.val
#         current = current.head

#     return sum


## sum_list(a)


# def linked_list_find(head, target):       # Find a specific node value
#   while head != None:
#     if head.val == target:
#       return True
#     head = head.next
  
#   return False


# def linked_list_find(head, target):        # Recursive
#   if head is None:
#     return False
#   if head.val == target:
#     return True
#   return linked_list_find(head.next, target)


## linked_list_find(a, "c") # True


# def get_node_value(head, index):            # Get Node value of a specific index
#   count = 0
#   current = head
  
#   while current != None:
#     if count == index:
#       return current.val
    
#     current = current.next
#     count += 1
    
#   return None


# def get_node_value(head, index):           # Recursive
#   if head is None:
#     return None
  
#   if index == 0:
#     return head.val
  
#   return get_node_value(head.next, index - 1)


## get_node_value(a, 2) # 'c'


# def reverse_list(head):             # Reverse the list
#     prev = None
#     current = head
#     while current != None:
#         current.next = prev
#         next = current.next
#         prev = current
#         current = next
#     return prev


# def reverse_list(head, prev=None):      # Recursion
#     if head == None: return prev
#     next = head.next
#     head.next = prev
#     reverse_list(next, head)

# reverse_list(a)


# def zipperlist(head1, head2):
#     tail = head1
#     current1 = head1.next
#     current2 = head2
#     count = 0

#     while (current1 != None and current2 != None):
#         if count % 2 == 0:
#             tail.next = current2
#             current2 = current2.next
#         else:
#             tail.next = current1
#             current2 = current1.next
#         tail = tail.next
#         count += 1

#         if current1 != None: tail.next = current1
#         if current2 != None: tail.next = current2

#     return head1


# def zipperlist(head1, head2):
#     if (head1 == None and head2 == None): return None

#     if head1 == None: return head2
#     if head2 == None: return head1

#     next1 = head1.next
#     next2 = head2.next
#     head1.next = head2
#     head2.next = zipperlist(next1, next2)

#     return head1