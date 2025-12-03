from typing import Dict, List, TypedDict

class ItemDetails(TypedDict):
    cost: int
    calories: int

class RatioItem(TypedDict):
    name: str
    cost: int
    calories: int
    ratio: float

items: Dict[str, ItemDetails] = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items: Dict[str, ItemDetails], budget: int) -> Dict[str, ItemDetails]:
    """
    Greedy algorithm to select dishes maximizing calorie-to-cost ratio.
    
    Args:
        items: Dictionary with dish names as keys and dict with cost and calories as values
        budget: Maximum budget available
        
    Returns:
        Dictionary with selected dishes and their details
    """
    # Calculate calorie-to-cost ratio for each item
    items_with_ratio: List[RatioItem] = []
    for name, details in items.items():
        ratio: float = details["calories"] / details["cost"]
        items_with_ratio.append({
            "name": name,
            "cost": details["cost"],
            "calories": details["calories"],
            "ratio": ratio
        })
    
    # Sort items by ratio in descending order
    items_with_ratio.sort(key=lambda x: x["ratio"], reverse=True)
    
    # Select items while budget allows
    selected_items: Dict[str, ItemDetails] = {}
    total_cost: int = 0
    total_calories: int = 0
    
    for item in items_with_ratio:
        if total_cost + item["cost"] <= budget:
            selected_items[item["name"]] = {
                "cost": item["cost"],
                "calories": item["calories"]
            }
            total_cost += item["cost"]
            total_calories += item["calories"]
    
    return selected_items


def dynamic_programming(items: Dict[str, ItemDetails], budget: int) -> Dict[str, ItemDetails]:
    """
    Dynamic programming algorithm to find optimal set of dishes for maximum calories.
    
    Args:
        items: Dictionary with dish names as keys and dict with cost and calories as values
        budget: Maximum budget available
        
    Returns:
        Dictionary with selected dishes and their details
    """
    # Convert items to lists for easier indexing
    item_names: List[str] = list(items.keys())
    n: int = len(item_names)
    
    # Create DP table
    dp: List[List[int]] = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        item_name: str = item_names[i - 1]
        cost: int = items[item_name]["cost"]
        calories: int = items[item_name]["calories"]
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find selected items
    selected_items: Dict[str, ItemDetails] = {}
    w: int = budget
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = item_names[i - 1]
            selected_items[item_name] = {
                "cost": items[item_name]["cost"],
                "calories": items[item_name]["calories"]
            }
            w -= items[item_name]["cost"]
            if w < 0:
                break
    
    return selected_items


if __name__ == "__main__":
    budget = 100
    
    print("\nGreedy Algorithm:")
    greedy_result = greedy_algorithm(items, budget)
    total_cost_greedy = sum(item["cost"] for item in greedy_result.values())
    total_calories_greedy = sum(item["calories"] for item in greedy_result.values())
    print(f"Selected items: {list(greedy_result.keys())}")
    print(f"Total cost: {total_cost_greedy}")
    print(f"Total calories: {total_calories_greedy}")
    
    print("\nDynamic Programming:")
    dp_result = dynamic_programming(items, budget)
    total_cost_dp = sum(item["cost"] for item in dp_result.values())
    total_calories_dp = sum(item["calories"] for item in dp_result.values())
    print(f"Selected items: {list(dp_result.keys())}")
    print(f"Total cost: {total_cost_dp}")
    print(f"Total calories: {total_calories_dp}")
