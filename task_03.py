import heapq


def min_connection_cost(cables):
    if len(cables) <= 1:
        return 0

    heap = cables.copy()
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        first_cable = heapq.heappop(heap)
        second_cable = heapq.heappop(heap)

        connection_cost = first_cable + second_cable
        total_cost += connection_cost

        heapq.heappush(heap, connection_cost)

    return total_cost


def run_tests():
    assert min_connection_cost([4, 3, 2, 6]) == 29
    assert min_connection_cost([1, 2, 3, 4, 5]) == 33
    assert min_connection_cost([8, 4, 6, 12]) == 58
    assert min_connection_cost([5]) == 0
    assert min_connection_cost([]) == 0


if __name__ == "__main__":
    run_tests()

    cables = [4, 3, 2, 6]

    print("Task 3")
    print("Cable lengths:", cables)
    print("Minimum total cost:", min_connection_cost(cables))
