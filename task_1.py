from typing import Optional, List


class Node:
    """Node class for singly linked list"""
    def __init__(self, val: int = 0):
        self.val = val
        self.next: Optional['Node'] = None


class LinkedList:
    """Singly linked list implementation"""
    def __init__(self):
        self.head = None
    
    def append(self, val: int) -> None:
        """Add a node at the end of the list"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self) -> List[int]:
        """Display the linked list as a list"""
        result: List[int] = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result


def reverse_linked_list(head: Optional[Node]) -> Optional[Node]:
    """
    Reverse a singly linked list by changing links between nodes.
    
    Args:
        head: Head node of the linked list
    
    Returns:
        New head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current           # Move prev pointer
        current = next_temp      # Move current pointer
    
    return prev  # prev becomes the new head


def insertion_sort_linked_list(head: Optional[Node]) -> Optional[Node]:
    """
    Sort a singly linked list using insertion sort algorithm.
    
    Args:
        head: Head node of the linked list
    
    Returns:
        Head of the sorted linked list
    """
    if not head or not head.next:
        return head
    
    # Create dummy node to simplify insertion
    dummy = Node(0)
    current = head
    
    while current:
        next_temp = current.next  # Store next node
        prev = dummy
        
        # Find the correct position to insert current node
        while prev.next and prev.next.val < current.val:
            prev = prev.next
        
        # Insert current node in the correct position
        current.next = prev.next
        prev.next = current
        
        current = next_temp  # Move to next node
    
    return dummy.next


def merge_sorted_lists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    """
    Merge two sorted linked lists into one sorted list.
    
    Args:
        list1: Head of the first sorted linked list
        list2: Head of the second sorted linked list
    
    Returns:
        Head of the merged sorted linked list
    """
    # Create dummy node to simplify merging
    dummy = Node(0)
    current = dummy
    
    # Compare nodes and merge in sorted order
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Add remaining nodes from either list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    return dummy.next


# Test functions
if __name__ == "__main__":
    list1 = LinkedList()
    for val in [14, 37, 63, 9, 15]:
        list1.append(val)
    print(f"\nOriginal first list: {list1.display()}")
    list1.head = reverse_linked_list(list1.head)
    print(f"Reversed first list: {list1.display()}")
    list1.head = insertion_sort_linked_list(list1.head)
    print(f"Sorted first list: {list1.display()}")

    list2 = LinkedList()
    for val in [42, 21, 48, 67, 10]:
        list2.append(val)
    print(f"\nOriginal second list: {list2.display()}")
    list2.head = reverse_linked_list(list2.head)
    print(f"Reversed second list: {list2.display()}")
    list2.head = insertion_sort_linked_list(list2.head)
    print(f"Sorted second list: {list2.display()}")

    # Test merge function
    merged_head = merge_sorted_lists(list1.head, list2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print(f"\nMerged sorted list: {merged_list.display()}")
