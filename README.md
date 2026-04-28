# Project 2: Moonlight Museum After Dark

## Team information
- Team name: Moonlight Coders
- Members: Aqush Limbu
- Repository name: week-7-moonlight-museum

---

## Project summary
Our project builds a system for organizing mysterious museum artifacts after dark.  
The system uses multiple data structures like a binary search tree, queue, stack, and linked list to manage artifacts, restoration requests, exhibit routes, and reports efficiently.

---

## Feature checklist

### Core structures
- [x] `Artifact` class/record
- [x] `ArtifactBST`
- [x] `RestorationQueue`
- [x] `ArchiveUndoStack`
- [x] `ExhibitRoute` singly linked list

### BST features
- [x] insert artifact
- [x] search by ID
- [x] preorder traversal
- [x] inorder traversal
- [x] postorder traversal
- [x] duplicate IDs ignored

### Queue features
- [x] add request
- [x] process next request
- [x] peek next request
- [x] empty check
- [x] size

### Stack features
- [x] push action
- [x] undo last action
- [x] peek last action
- [x] empty check
- [x] size

### Linked list features
- [x] add stop to end
- [x] remove first matching stop
- [x] list stops in order
- [x] count stops

### Utility/report features
- [x] category counts
- [x] unique rooms
- [x] sort by age
- [x] linear search by name

### Integration
- [x] `demo_museum_night()`
- [x] at least 8 artifacts in demo
- [x] demo shows system parts working together

---

## Design note (150–250 words)

This project uses multiple data structures to efficiently manage different aspects of the museum system. A binary search tree (BST) is used for storing artifacts because it allows fast searching, insertion, and ordered traversal based on artifact IDs. This is important for quickly locating artifacts in a large archive.

A queue is used for restoration requests because it follows the FIFO (First-In-First-Out) principle. This ensures that older requests are processed before newer ones, which reflects real-world fairness in task handling.

A stack is used for undo actions because it follows the LIFO (Last-In-First-Out) principle. The most recent action is undone first, which matches how undo systems work in applications.

A singly linked list is used for the exhibit route because it allows easy addition and removal of stops while maintaining order. It is memory efficient and simple for sequential navigation.

Overall, the system is modular, with each class handling a specific responsibility. Utility functions are separated for reporting tasks like sorting, counting, and searching. This makes the system organized, readable, and easy to maintain.

---

## Complexity reasoning

- `ArtifactBST.insert`: `O(h)` where `h` is tree height, because we traverse one path down the tree.
- `ArtifactBST.search_by_id`: `O(h)` because it follows one branch from root to leaf.
- `ArtifactBST.inorder_ids`: `O(n)` because every node is visited once.
- `RestorationQueue.process_next_request`: `O(1)` because deque pop from front is constant time.
- `ArchiveUndoStack.undo_last_action`: `O(1)` because list pop from end is constant time.
- `ExhibitRoute.remove_stop`: `O(n)` because we may need to traverse the entire list.
- `sort_artifacts_by_age`: `O(n log n)` due to Python’s sorting algorithm.
- `linear_search_by_name`: `O(n)` because it checks each artifact one by one.

---

## Edge-case checklist

### BST
- [x] insert into empty tree → creates root
- [x] search for missing ID → returns None
- [x] empty traversals → return empty list
- [x] duplicate ID → ignored

### Queue
- [x] process empty queue → returns None
- [x] peek empty queue → returns None

### Stack
- [x] undo empty stack → returns None
- [x] peek empty stack → returns None

### Exhibit route linked list
- [x] empty route → returns empty list
- [x] remove missing stop → returns False
- [x] remove first stop → updates head
- [x] remove middle stop → reconnects nodes
- [x] remove last stop → removes tail
- [x] one-stop route → becomes empty

### Reports
- [x] empty artifact list → returns empty result
- [x] repeated categories → counted correctly
- [x] repeated rooms → removed using set
- [x] missing artifact name → returns None
- [x] same-age artifacts → handled by sorting

---

## Demo plan / how to run

Run tests:
```bash
pytest -q