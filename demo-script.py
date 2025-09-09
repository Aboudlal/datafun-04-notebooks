'''
Optional: This is just to test key code with a script. 
'''

#####################################
# Import Modules at the Top
#####################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets  # interactive widgets
from IPython.display import display  # used for display of widgets

#####################################
# Chart Functions
#####################################

def plot_scatter_plot(penguins_df: pd.DataFrame):
    """Create and display a scatter plot for the Penguins dataset."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=penguins_df, x="flipper_length_mm", y="body_mass_g", hue="species", ax=ax
    )
    ax.set_xlabel("Flipper Length (mm)")
    ax.set_ylabel("Body Mass (g)")
    ax.set_title("Chart 1. Penguin Flipper Length vs. Body Mass (by Species)")
    return fig


def plot_bar_chart(sales_df: pd.DataFrame):
    """Create and display a bar chart for the sales dataset."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="Category", y="Sales", data=sales_df, ax=ax)
    ax.set_title("Chart 2. Sales by Category")
    return fig


def create_interactive_histogram():
    """Create and display an interactive histogram with ipywidgets."""
    # Generate sample data
    np.random.seed(42)
    sample_data_array = np.random.normal(loc=170, scale=10, size=1000)

    # Function to plot the histogram
    def plot_histogram(count_of_bins: int = 10):
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(sample_data_array, bins=count_of_bins, color="skyblue", edgecolor="black")
        ax.set_title("Chart 3. Interactive Histogram (use slider to change number of bins)")
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

    # Create an interactive slider
    bins_slider = widgets.IntSlider(value=10, min=5, max=50, step=1, description="Bins:")
    interactive_hist = widgets.interactive(plot_histogram, count_of_bins=bins_slider)
    display(bins_slider, interactive_hist)


#####################################
# Main Execution
#####################################

def main():
    # Chart 1 - Scatter Plot: Passengers over Time (by Month)
    print("Creating Chart 1: Scatter Plot...")
    flights_df = sns.load_dataset("flights")
    _ = sns.scatterplot(
        data=flights_df, 
        x="year", 
        y="passengers", 
        hue="month"
    ).set_title("Chart 1. Airline Passenger Traffic Over Time (by Month)")

    # Chart 2 - Bar Chart: Total Passengers per Year
    print("Creating Chart 2: Bar Chart...")
    yearly_passengers = flights_df.groupby("year")["passengers"].sum().reset_index()
    _ = sns.barplot(
        x="year", 
        y="passengers", 
        data=yearly_passengers
    ).set_title("Chart 2. Total Airline Passengers by Year")

    # Display static charts together
    print("Displaying static charts...")
    plt.show()


    # Chart 3 - Interactive Histogram
    print("Creating Chart 3: Interactive Histogram...")
    create_interactive_histogram()


if __name__ == "__main__":
    main()
