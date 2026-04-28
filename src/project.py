"""Project 2 starter code: Moonlight Museum After Dark.

Students should implement all required behavior in this file.
Use stdlib only.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    artifact_id: int
    description: str


class TreeNode:
    def __init__(
        self,
        artifact: Artifact,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.artifact = artifact
        self.left = left
        self.right = right


class ArtifactBST:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, artifact: Artifact) -> bool:
        if self.root is None:
            self.root = TreeNode(artifact)
            return True

        current = self.root
        while True:
            if artifact.artifact_id == current.artifact.artifact_id:
                return False
            elif artifact.artifact_id < current.artifact.artifact_id:
                if current.left is None:
                    current.left = TreeNode(artifact)
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(artifact)
                    return True
                current = current.right

    def search_by_id(self, artifact_id: int) -> Artifact | None:
        current = self.root
        while current:
            if artifact_id == current.artifact.artifact_id:
                return current.artifact
            elif artifact_id < current.artifact.artifact_id:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_ids(self) -> list[int]:
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.artifact.artifact_id)
                traverse(node.right)

        traverse(self.root)
        return result

    def preorder_ids(self) -> list[int]:
        result = []

        def traverse(node):
            if node:
                result.append(node.artifact.artifact_id)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def postorder_ids(self) -> list[int]:
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.artifact.artifact_id)

        traverse(self.root)
        return result


class RestorationQueue:
    def __init__(self) -> None:
        self._items: Deque[RestorationRequest] = deque()

    def add_request(self, request: RestorationRequest) -> None:
        self._items.append(request)

    def process_next_request(self) -> RestorationRequest | None:
        if self._items:
            return self._items.popleft()
        return None

    def peek_next_request(self) -> RestorationRequest | None:
        if self._items:
            return self._items[0]
        return None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ArchiveUndoStack:
    def __init__(self) -> None:
        self._items: list[str] = []

    def push_action(self, action: str) -> None:
        self._items.append(action)

    def undo_last_action(self) -> str | None:
        if self._items:
            return self._items.pop()
        return None

    def peek_last_action(self) -> str | None:
        if self._items:
            return self._items[-1]
        return None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ExhibitNode:
    def __init__(self, stop_name: str, next_node: ExhibitNode | None = None) -> None:
        self.stop_name = stop_name
        self.next = next_node


class ExhibitRoute:
    def __init__(self) -> None:
        self.head: ExhibitNode | None = None

    def add_stop(self, stop_name: str) -> None:
        new_node = ExhibitNode(stop_name)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_stop(self, stop_name: str) -> bool:
        current = self.head
        prev = None

        while current:
            if current.stop_name == stop_name:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

    def list_stops(self) -> list[str]:
        result = []
        current = self.head
        while current:
            result.append(current.stop_name)
            current = current.next
        return result

    def count_stops(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


def count_artifacts_by_category(artifacts: list[Artifact]) -> dict[str, int]:
    counts = {}
    for art in artifacts:
        counts[art.category] = counts.get(art.category, 0) + 1
    return counts


def unique_rooms(artifacts: list[Artifact]) -> set[str]:
    return {art.room for art in artifacts}


def sort_artifacts_by_age(
    artifacts: list[Artifact],
    descending: bool = False,
) -> list[Artifact]:
    return sorted(artifacts, key=lambda a: a.age, reverse=descending)


def linear_search_by_name(
    artifacts: list[Artifact],
    name: str,
) -> Artifact | None:
    for art in artifacts:
        if art.name == name:
            return art
    return None


def demo_museum_night() -> None:
    bst = ArtifactBST()

    artifacts = [
        Artifact(3, "Vase", "Ceramics", 200, "A1"),
        Artifact(1, "Sword", "Weapons", 500, "B2"),
        Artifact(5, "Painting", "Art", 100, "C3"),
    ]

    for a in artifacts:
        bst.insert(a)

    print("Inorder IDs:", bst.inorder_ids())

    queue = RestorationQueue()
    queue.add_request(RestorationRequest(1, "Polish blade"))
    queue.add_request(RestorationRequest(3, "Repair crack"))

    print("Next request:", queue.peek_next_request())
    print("Processing:", queue.process_next_request())

    stack = ArchiveUndoStack()
    stack.push_action("Added Sword")
    stack.push_action("Removed Vase")

    print("Undo:", stack.undo_last_action())

    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("Gallery A")
    route.add_stop("Gallery B")

    print("Route:", route.list_stops())

    print("Category count:", count_artifacts_by_category(artifacts))
    print("Unique rooms:", unique_rooms(artifacts))

    sorted_arts = sort_artifacts_by_age(artifacts)
    print("Sorted by age:", [a.name for a in sorted_arts])

    found = linear_search_by_name(artifacts, "Sword")
    print("Search result:", found)


if __name__ == "__main__":
    demo_museum_night()