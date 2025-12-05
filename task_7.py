import numpy as np
import matplotlib.pyplot as plt


def simulate_dice_rolls(n_trials: int) -> dict[int, int]:
    """
    Simulate rolling two six-sided dice many times.

    Parameters
    ----------
    n_trials : int
        Number of dice roll simulations.

    Returns
    -------
    dict[int, int]
        Dictionary where keys are sums (2-12) and values are counts
        of how many times each sum appeared.
    """
    rng = np.random.default_rng()

    # Generate random integers from 1 to 6 for two dice
    dice1 = rng.integers(1, 7, size=n_trials)
    dice2 = rng.integers(1, 7, size=n_trials)

    # Calculate sums of two dice
    sums = dice1 + dice2

    # Count occurrences of each sum from 2 to 12
    counts = {total: 0 for total in range(2, 13)}
    for value in sums:
        counts[value] += 1

    return counts


def calculate_probabilities(
    counts: dict[int, int],
    n_trials: int,
) -> dict[int, float]:
    """
    Calculate probabilities of each sum from simulation results.

    Parameters
    ----------
    counts : dict[int, int]
        Counts of each sum (2-12) from simulations.
    n_trials : int
        Total number of trials.

    Returns
    -------
    dict[int, float]
        Dictionary where keys are sums (2-12) and values are
        estimated probabilities.
    """
    return {total: count / n_trials for total, count in counts.items()}


def theoretical_probabilities() -> dict[int, float]:
    """
    Return theoretical probabilities for sums when rolling two dice.

    Probabilities are based on all 36 equally likely outcomes.

    Returns
    -------
    dict[int, float]
        Dictionary of exact probabilities for sums 2-12.
    """
    # Number of combinations giving each sum
    combinations = {
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 5,
        9: 4,
        10: 3,
        11: 2,
        12: 1,
    }

    total_outcomes = 36
    return {
        total: count / total_outcomes
        for total, count in combinations.items()
    }


def print_detailed_probability_table(
    simulated: dict[int, float],
    theoretical: dict[int, float],
    n_trials: int,
) -> None:
    """
    Print detailed table comparing Monte Carlo and theoretical probabilities.

    Parameters
    ----------
    simulated : dict[int, float]
        Probabilities estimated via Monte Carlo simulation.
    theoretical : dict[int, float]
        Exact theoretical probabilities.
    n_trials : int
        Total number of trials performed.
    """
    print(f"\nMonte Carlo Dice Simulation Results ({n_trials:,} throws)")
    print("=" * 85)
    
    header = (
        f"{'Sum':<4} | {'Monte Carlo':<15} | {'Theoretical':<15} | "
        f"{'Difference':<12} | {'Abs Diff':<10}"
    )
    print(header)
    print("-" * 85)

    total_abs_diff = 0
    for total in range(2, 13):
        sim_p = simulated[total]
        theo_p = theoretical[total]
        diff = sim_p - theo_p
        abs_diff = abs(diff)
        total_abs_diff += abs_diff
        
        print(
            f"{total:<4} | "
            f"{sim_p*100:>6.2f}% ({sim_p:.4f}) | "
            f"{theo_p*100:>6.2f}% ({theo_p:.4f}) | "
            f"{diff*100:>+8.4f}% | "
            f"{abs_diff*100:>6.4f}%"
        )
    
    avg_abs_diff = total_abs_diff / 11
    print("-" * 85)
    print(f"Average absolute difference: {avg_abs_diff*100:.4f}%")
    
    # Find most and least likely sums
    most_likely = max(simulated.keys(), key=lambda x: simulated[x])
    least_likely = min(simulated.keys(), key=lambda x: simulated[x])
    
    print(f"Most likely sum (Monte Carlo): {most_likely} ({simulated[most_likely]*100:.2f}%)")
    print(f"Least likely sum (Monte Carlo): {least_likely} ({simulated[least_likely]*100:.2f}%)")


def create_probability_visualization(
    simulated: dict[int, float],
    theoretical: dict[int, float],
    n_trials: int,
) -> None:
    """
    Create visualization comparing Monte Carlo and theoretical probabilities.

    Parameters
    ----------
    simulated : dict[int, float]
        Probabilities estimated via Monte Carlo simulation.
    theoretical : dict[int, float]
        Exact theoretical probabilities.
    n_trials : int
        Total number of trials performed.
    """
    sums = list(range(2, 13))
    sim_values = [simulated[s] * 100 for s in sums]  # Convert to percentages
    theo_values = [theoretical[s] * 100 for s in sums]
    
    # Create single figure
    plt.figure(figsize=(12, 8))
    
    # Bar chart comparison
    x_positions = range(len(sums))
    bar_width = 0.35
    
    bars1 = plt.bar([x - bar_width/2 for x in x_positions], sim_values, bar_width,
                    label=f'Monte Carlo ({n_trials:,} trials)', 
                    alpha=0.8, color='skyblue', edgecolor='darkblue', linewidth=1)
    bars2 = plt.bar([x + bar_width/2 for x in x_positions], theo_values, bar_width,
                    label='Theoretical', alpha=0.8, color='lightcoral', 
                    edgecolor='darkred', linewidth=1)
    
    # Add value labels on bars with better positioning and formatting
    max_height = max(max(sim_values), max(theo_values))
    label_offset = max_height * 0.015  # Dynamic offset based on max height
    
    for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
        # Monte Carlo labels with better positioning
        plt.text(bar1.get_x() + bar1.get_width()/2, bar1.get_height() + label_offset, 
                f'{sim_values[i]:.1f}%', ha='center', va='bottom', 
                fontsize=11, fontweight='bold', color='darkblue', 
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
        # Theoretical labels with better positioning
        plt.text(bar2.get_x() + bar2.get_width()/2, bar2.get_height() + label_offset, 
                f'{theo_values[i]:.1f}%', ha='center', va='bottom', 
                fontsize=11, fontweight='bold', color='darkred',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
    
    plt.xlabel('Sum of Two Dice', fontsize=14, fontweight='bold')
    plt.ylabel('Probability (%)', fontsize=14, fontweight='bold')
    plt.title('Monte Carlo vs Theoretical Probabilities for Dice Sums', 
             fontsize=16, fontweight='bold', pad=20)
    plt.xticks(x_positions, [str(s) for s in sums], fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=13, loc='upper right')
    plt.grid(True, alpha=0.3, axis='y', linestyle='--')
    plt.ylim(0, max_height * 1.25)  # Give more space for labels
    
    # Add background color for better contrast
    plt.gca().set_facecolor('#f9f9f9')
    
    plt.tight_layout()
    plt.show()

def main() -> None:
    """
    Run Monte Carlo simulation for dice rolls with detailed analysis and visualization.

    The program:
    1. Simulates rolling two dice many times.
    2. Counts occurrences of each possible sum (2-12).
    3. Calculates Monte Carlo probabilities.
    4. Compares them with theoretical probabilities in detailed table.
    5. Creates visualization showing probability comparison and differences.
    """
    n_trials = 1_000_000  # Large number of simulations
    
    print("Monte Carlo Method: Dice Throwing Simulation")
    print("=" * 50)
    print(f"Simulating {n_trials:,} dice throws using NumPy vectorization...")

    # Step 1: simulate rolls and count sums
    counts = simulate_dice_rolls(n_trials)

    # Step 2: calculate Monte Carlo probabilities
    simulated_probs = calculate_probabilities(counts, n_trials)

    # Step 3: get theoretical probabilities
    theoretical_probs = theoretical_probabilities()

    # Step 4: print detailed comparison table
    print_detailed_probability_table(simulated_probs, theoretical_probs, n_trials)
    
    # Step 5: create visualization
    create_probability_visualization(simulated_probs, theoretical_probs, n_trials)
    

if __name__ == "__main__":
    main()
