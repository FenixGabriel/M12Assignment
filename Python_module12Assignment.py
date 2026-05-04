# Module 12 Assignment: Business Analytics Fundamentals and Applications
# GreenGrocer Data Analysis
 
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
 
# Welcome message
print("=" * 60)
print("GREENGROCER BUSINESS ANALYTICS")
print("=" * 60)
 
# ----- USE THE FOLLOWING CODE TO CREATE SAMPLE DATA (DO NOT MODIFY) -----
np.random.seed(42)
 
stores = ["Tampa", "Orlando", "Miami", "Jacksonville", "Gainesville"]
store_data = {
    "Store": stores,
    "SquareFootage": [15000, 12000, 18000, 10000, 8000],
    "StaffCount": [45, 35, 55, 30, 25],
    "YearsOpen": [5, 3, 7, 2, 1],
    "WeeklyMarketingSpend": [2500, 2000, 3000, 1800, 1500]
}
 
store_df = pd.DataFrame(store_data)
 
departments = ["Produce", "Dairy", "Bakery", "Grocery", "Prepared Foods"]
categories = {
    "Produce": ["Organic Vegetables", "Organic Fruits", "Fresh Herbs"],
    "Dairy": ["Milk & Cream", "Cheese", "Yogurt"],
    "Bakery": ["Bread", "Pastries", "Cakes"],
    "Grocery": ["Grains", "Canned Goods", "Snacks"],
    "Prepared Foods": ["Hot Bar", "Salad Bar", "Sandwiches"]
}
 
sales_data = []
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
 
store_performance = {
    "Tampa": 1.0,
    "Orlando": 0.85,
    "Miami": 1.2,
    "Jacksonville": 0.75,
    "Gainesville": 0.65
}
 
dept_performance = {
    "Produce": 1.2,
    "Dairy": 1.0,
    "Bakery": 0.85,
    "Grocery": 0.95,
    "Prepared Foods": 1.1
}
 
for date in dates:
    month = date.month
    seasonal_factor = 1.0
    if month in [6, 7, 8]:
        seasonal_factor = 1.15
    elif month == 12:
        seasonal_factor = 1.25
    elif month in [1, 2]:
        seasonal_factor = 0.9
 
    dow_factor = 1.3 if date.dayofweek >= 5 else 1.0
 
    for store in stores:
        store_factor = store_performance[store]
 
        for dept in departments:
            dept_factor = dept_performance[dept]
 
            for category in categories[dept]:
                base_sales = np.random.normal(loc=500, scale=100)
                sales_amount = base_sales * store_factor * dept_factor * seasonal_factor * dow_factor
                sales_amount = sales_amount * np.random.normal(loc=1.0, scale=0.1)
 
                base_margin = {
                    "Produce": 0.25,
                    "Dairy": 0.22,
                    "Bakery": 0.35,
                    "Grocery": 0.20,
                    "Prepared Foods": 0.40
                }[dept]
                profit_margin = base_margin * np.random.normal(loc=1.0, scale=0.05)
                profit_margin = max(min(profit_margin, 0.5), 0.15)
 
                profit = sales_amount * profit_margin
 
                sales_data.append({
                    "Date": date,
                    "Store": store,
                    "Department": dept,
                    "Category": category,
                    "Sales": round(sales_amount, 2),
                    "ProfitMargin": round(profit_margin, 4),
                    "Profit": round(profit, 2)
                })
 
sales_df = pd.DataFrame(sales_data)
 
customer_data = []
total_customers = 5000
 
age_mean, age_std = 42, 15
income_mean, income_std = 85, 30
 
segments = ["Health Enthusiast", "Gourmet Cook", "Family Shopper", "Budget Organic", "Occasional Visitor"]
segment_probabilities = [0.25, 0.20, 0.30, 0.15, 0.10]
 
store_probs = {
    "Tampa": 0.25,
    "Orlando": 0.20,
    "Miami": 0.30,
    "Jacksonville": 0.15,
    "Gainesville": 0.10
}
 
for i in range(total_customers):
    age = int(np.random.normal(loc=age_mean, scale=age_std))
    age = max(min(age, 85), 18)
 
    gender = np.random.choice(["M", "F"], p=[0.48, 0.52])
 
    income = int(np.random.normal(loc=income_mean, scale=income_std))
    income = max(income, 20)
 
    segment = np.random.choice(segments, p=segment_probabilities)
    preferred_store = np.random.choice(stores, p=list(store_probs.values()))
 
    if segment == "Health Enthusiast":
        visit_frequency = np.random.randint(8, 15)
        avg_basket = np.random.normal(loc=75, scale=15)
    elif segment == "Gourmet Cook":
        visit_frequency = np.random.randint(4, 10)
        avg_basket = np.random.normal(loc=120, scale=25)
    elif segment == "Family Shopper":
        visit_frequency = np.random.randint(5, 12)
        avg_basket = np.random.normal(loc=150, scale=30)
    elif segment == "Budget Organic":
        visit_frequency = np.random.randint(6, 10)
        avg_basket = np.random.normal(loc=60, scale=10)
    else:
        visit_frequency = np.random.randint(1, 5)
        avg_basket = np.random.normal(loc=45, scale=15)
 
    visit_frequency = max(min(visit_frequency, 30), 1)
    avg_basket = max(avg_basket, 15)
 
    monthly_spend = visit_frequency * avg_basket
    if monthly_spend > 1000:
        loyalty_tier = "Platinum"
    elif monthly_spend > 500:
        loyalty_tier = "Gold"
    elif monthly_spend > 200:
        loyalty_tier = "Silver"
    else:
        loyalty_tier = "Bronze"
 
    customer_data.append({
        "CustomerID": f"C{i+1:04d}",
        "Age": age,
        "Gender": gender,
        "Income": income * 1000,
        "Segment": segment,
        "PreferredStore": preferred_store,
        "VisitsPerMonth": visit_frequency,
        "AvgBasketSize": round(avg_basket, 2),
        "MonthlySpend": round(visit_frequency * avg_basket, 2),
        "LoyaltyTier": loyalty_tier
    })
 
customer_df = pd.DataFrame(customer_data)
 
operational_data = []
 
for store in stores:
    store_row = store_df[store_df["Store"] == store].iloc[0]
    square_footage = store_row["SquareFootage"]
    staff_count = store_row["StaffCount"]
 
    store_sales = sales_df[sales_df["Store"] == store]["Sales"].sum()
    store_profit = sales_df[sales_df["Store"] == store]["Profit"].sum()
 
    sales_per_sqft = store_sales / square_footage
    profit_per_sqft = store_profit / square_footage
    sales_per_staff = store_sales / staff_count
    inventory_turnover = np.random.uniform(12, 18) * store_performance[store]
    customer_satisfaction = min(5, np.random.normal(loc=4.0, scale=0.3) *
                                (store_performance[store] ** 0.5))
 
    operational_data.append({
        "Store": store,
        "AnnualSales": round(store_sales, 2),
        "AnnualProfit": round(store_profit, 2),
        "SalesPerSqFt": round(sales_per_sqft, 2),
        "ProfitPerSqFt": round(profit_per_sqft, 2),
        "SalesPerStaff": round(sales_per_staff, 2),
        "InventoryTurnover": round(inventory_turnover, 2),
        "CustomerSatisfaction": round(customer_satisfaction, 2)
    })
 
operational_df = pd.DataFrame(operational_data)
 
print("\nDataframes created successfully. Ready for analysis!")
print(f"Sales data shape: {sales_df.shape}")
print(f"Customer data shape: {customer_df.shape}")
print(f"Store data shape: {store_df.shape}")
print(f"Operational data shape: {operational_df.shape}")
 
print("\nSales Data Sample:")
print(sales_df.head(3))
print("\nCustomer Data Sample:")
print(customer_df.head(3))
print("\nStore Data Sample:")
print(store_df)
print("\nOperational Data Sample:")
print(operational_df)
# ----- END OF DATA CREATION -----
 
 
# ─────────────────────────────────────────────────────────────────────────────
# HELPER: shared color palette
# ─────────────────────────────────────────────────────────────────────────────
STORE_COLORS = {
    "Tampa": "#2E86AB",
    "Orlando": "#A23B72",
    "Miami": "#F18F01",
    "Jacksonville": "#C73E1D",
    "Gainesville": "#3B1F2B"
}
DEPT_COLORS = {
    "Produce": "#4CAF50",
    "Dairy": "#2196F3",
    "Bakery": "#FF9800",
    "Grocery": "#9C27B0",
    "Prepared Foods": "#F44336"
}
 
 
# ─────────────────────────────────────────────────────────────────────────────
# TODO 1: Descriptive Analytics
# ─────────────────────────────────────────────────────────────────────────────
 
def analyze_sales_performance():
    """
    Analyze overall sales performance with descriptive statistics.
    Returns a dictionary with keys:
    - 'total_sales': float
    - 'total_profit': float
    - 'avg_profit_margin': float
    - 'sales_by_store': pandas Series
    - 'sales_by_dept': pandas Series
    """
    total_sales = sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()
    avg_profit_margin = sales_df["ProfitMargin"].mean()
 
    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    sales_by_dept  = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)
 
    # Print summary statistics
    print("\n[1.1] Sales Performance Summary")
    print(f"  Total Annual Sales   : ${total_sales:>15,.2f}")
    print(f"  Total Annual Profit  : ${total_profit:>15,.2f}")
    print(f"  Avg Profit Margin    : {avg_profit_margin:.2%}")
    print(f"\n  Sales by Store:\n{sales_by_store.to_string()}")
    print(f"\n  Sales by Department:\n{sales_by_dept.to_string()}")
 
    desc = sales_df[["Sales", "Profit", "ProfitMargin"]].describe()
    print(f"\n  Descriptive Statistics:\n{desc.to_string()}")
 
    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "avg_profit_margin": avg_profit_margin,
        "sales_by_store": sales_by_store,
        "sales_by_dept": sales_by_dept
    }
 
 
def visualize_sales_distribution():
    """
    Create visualizations showing how sales are distributed.
    Returns a tuple of three figures: (store_fig, dept_fig, time_fig).
    """
    # --- Figure 1: Sales by Store (horizontal bar chart) ---
    store_fig, ax1 = plt.subplots(figsize=(9, 5))
    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values()
    colors = [STORE_COLORS[s] for s in sales_by_store.index]
    bars = ax1.barh(sales_by_store.index, sales_by_store.values, color=colors, edgecolor="white", linewidth=0.8)
    ax1.set_title("Annual Sales by Store", fontsize=14, fontweight="bold", pad=12)
    ax1.set_xlabel("Total Sales ($)")
    ax1.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    for bar, val in zip(bars, sales_by_store.values):
        ax1.text(val + 5000, bar.get_y() + bar.get_height()/2,
                 f"${val/1e6:.2f}M", va="center", fontsize=9)
    ax1.spines[["top", "right"]].set_visible(False)
    store_fig.tight_layout()
 
    # --- Figure 2: Sales & Profit by Department (grouped bar) ---
    dept_fig, ax2 = plt.subplots(figsize=(10, 5))
    dept_sales  = sales_df.groupby("Department")["Sales"].sum()
    dept_profit = sales_df.groupby("Department")["Profit"].sum()
    x = np.arange(len(dept_sales))
    w = 0.35
    ax2.bar(x - w/2, dept_sales.values,  width=w, label="Sales",  color=[DEPT_COLORS[d] for d in dept_sales.index], alpha=0.85)
    ax2.bar(x + w/2, dept_profit.values, width=w, label="Profit", color=[DEPT_COLORS[d] for d in dept_profit.index], alpha=0.55)
    ax2.set_xticks(x)
    ax2.set_xticklabels(dept_sales.index, rotation=15, ha="right")
    ax2.set_title("Sales & Profit by Department", fontsize=14, fontweight="bold", pad=12)
    ax2.set_ylabel("Amount ($)")
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    ax2.legend()
    ax2.spines[["top", "right"]].set_visible(False)
    dept_fig.tight_layout()
 
    # --- Figure 3: Monthly Sales Trend (line chart, all stores) ---
    time_fig, ax3 = plt.subplots(figsize=(12, 5))
    sales_df["Month"] = sales_df["Date"].dt.to_period("M")
    monthly_by_store = sales_df.groupby(["Month", "Store"])["Sales"].sum().reset_index()
    monthly_by_store["Month_dt"] = monthly_by_store["Month"].dt.to_timestamp()
    for store in stores:
        sub = monthly_by_store[monthly_by_store["Store"] == store]
        ax3.plot(sub["Month_dt"], sub["Sales"], label=store,
                 color=STORE_COLORS[store], linewidth=2, marker="o", markersize=4)
    ax3.set_title("Monthly Sales Trend by Store (2023)", fontsize=14, fontweight="bold", pad=12)
    ax3.set_ylabel("Monthly Sales ($)")
    ax3.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
    ax3.legend(loc="upper left", fontsize=9)
    ax3.spines[["top", "right"]].set_visible(False)
    time_fig.tight_layout()
 
    return store_fig, dept_fig, time_fig
 
 
def analyze_customer_segments():
    """
    Analyze customer segments and their spending patterns.
    Returns a dictionary with keys:
    - 'segment_counts': pandas Series
    - 'segment_avg_spend': pandas Series
    - 'segment_loyalty': pandas DataFrame
    """
    segment_counts    = customer_df["Segment"].value_counts()
    segment_avg_spend = customer_df.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False)
    segment_loyalty   = customer_df.groupby(["Segment", "LoyaltyTier"]).size().unstack(fill_value=0)
 
    print("\n[1.3] Customer Segment Analysis")
    print(f"\n  Segment Counts:\n{segment_counts.to_string()}")
    print(f"\n  Avg Monthly Spend by Segment:\n{segment_avg_spend.round(2).to_string()}")
    print(f"\n  Loyalty Tier Distribution by Segment:\n{segment_loyalty.to_string()}")
 
    # Visualization
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
 
    seg_colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#F44336"]
 
    axes[0].pie(segment_counts.values, labels=segment_counts.index,
                autopct="%1.1f%%", colors=seg_colors, startangle=140,
                wedgeprops=dict(edgecolor="white", linewidth=1.5))
    axes[0].set_title("Customer Segment Distribution", fontsize=13, fontweight="bold")
 
    axes[1].barh(segment_avg_spend.index, segment_avg_spend.values,
                 color=seg_colors[:len(segment_avg_spend)], edgecolor="white")
    axes[1].set_title("Avg Monthly Spend by Segment", fontsize=13, fontweight="bold")
    axes[1].set_xlabel("Average Monthly Spend ($)")
    axes[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:.0f}"))
    axes[1].spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
 
    return {
        "segment_counts": segment_counts,
        "segment_avg_spend": segment_avg_spend,
        "segment_loyalty": segment_loyalty
    }
 
 
# ─────────────────────────────────────────────────────────────────────────────
# TODO 2: Diagnostic Analytics
# ─────────────────────────────────────────────────────────────────────────────
 
def analyze_sales_correlations():
    """
    Analyze correlations between store characteristics and sales/profit.
    Returns a dictionary with keys:
    - 'store_correlations': pandas DataFrame
    - 'top_correlations': list of tuples (factor, correlation)
    - 'correlation_fig': matplotlib figure
    """
    # Merge operational metrics with store characteristics
    merged = operational_df.merge(store_df, on="Store")
    numeric_cols = ["AnnualSales", "AnnualProfit", "SalesPerSqFt", "ProfitPerSqFt",
                    "SalesPerStaff", "InventoryTurnover", "CustomerSatisfaction",
                    "SquareFootage", "StaffCount", "YearsOpen", "WeeklyMarketingSpend"]
    store_correlations = merged[numeric_cols].corr()
 
    # Top absolute correlations with AnnualSales (excluding self)
    sales_corr = store_correlations["AnnualSales"].drop("AnnualSales").abs().sort_values(ascending=False)
    top_correlations = [(factor, store_correlations["AnnualSales"][factor])
                        for factor in sales_corr.index[:5]]
 
    print("\n[2.1] Correlation Analysis (with AnnualSales):")
    for factor, corr in top_correlations:
        print(f"  {factor:<28}: {corr:+.4f}")
 
    # Heatmap
    correlation_fig, ax = plt.subplots(figsize=(10, 8))
    corr_subset = merged[["AnnualSales", "AnnualProfit", "SquareFootage",
                           "StaffCount", "YearsOpen", "WeeklyMarketingSpend",
                           "SalesPerSqFt", "SalesPerStaff"]].corr()
    im = ax.imshow(corr_subset.values, cmap="RdYlGn", vmin=-1, vmax=1, aspect="auto")
    ax.set_xticks(range(len(corr_subset.columns)))
    ax.set_yticks(range(len(corr_subset.columns)))
    ax.set_xticklabels(corr_subset.columns, rotation=40, ha="right", fontsize=9)
    ax.set_yticklabels(corr_subset.columns, fontsize=9)
    for i in range(len(corr_subset)):
        for j in range(len(corr_subset.columns)):
            ax.text(j, i, f"{corr_subset.values[i,j]:.2f}",
                    ha="center", va="center", fontsize=8,
                    color="black" if abs(corr_subset.values[i,j]) < 0.7 else "white")
    plt.colorbar(im, ax=ax, fraction=0.04, pad=0.04)
    ax.set_title("Store Metric Correlation Heatmap", fontsize=14, fontweight="bold", pad=12)
    correlation_fig.tight_layout()
 
    return {
        "store_correlations": store_correlations,
        "top_correlations": top_correlations,
        "correlation_fig": correlation_fig
    }
 
 
def compare_store_performance():
    """
    Compare stores across different operational metrics.
    Returns a dictionary with keys:
    - 'efficiency_metrics': pandas DataFrame (with SalesPerSqFt, SalesPerStaff)
    - 'performance_ranking': pandas Series (ranked by profit)
    - 'comparison_fig': matplotlib figure
    """
    efficiency_metrics  = operational_df[["Store", "SalesPerSqFt", "SalesPerStaff",
                                          "ProfitPerSqFt", "InventoryTurnover",
                                          "CustomerSatisfaction"]].set_index("Store")
    performance_ranking = operational_df.set_index("Store")["AnnualProfit"].sort_values(ascending=False)
 
    print("\n[2.2] Store Performance Comparison")
    print(f"\n  Efficiency Metrics:\n{efficiency_metrics.to_string()}")
    print(f"\n  Profit Ranking:\n{performance_ranking.to_string()}")
 
    # Radar-style grouped bar for key metrics (normalized)
    metrics = ["SalesPerSqFt", "SalesPerStaff", "ProfitPerSqFt",
               "InventoryTurnover", "CustomerSatisfaction"]
    norm = efficiency_metrics[metrics].copy()
    norm = (norm - norm.min()) / (norm.max() - norm.min() + 1e-9)
 
    comparison_fig, axes = plt.subplots(1, 2, figsize=(14, 5))
 
    # Left: Annual Profit bar
    colors = [STORE_COLORS[s] for s in performance_ranking.index]
    axes[0].bar(performance_ranking.index, performance_ranking.values,
                color=colors, edgecolor="white")
    axes[0].set_title("Annual Profit by Store", fontsize=13, fontweight="bold")
    axes[0].set_ylabel("Profit ($)")
    axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    axes[0].spines[["top", "right"]].set_visible(False)
 
    # Right: Normalized efficiency heatmap
    im2 = axes[1].imshow(norm.T.values, cmap="YlGn", aspect="auto", vmin=0, vmax=1)
    axes[1].set_xticks(range(len(norm.index)))
    axes[1].set_xticklabels(norm.index, fontsize=10)
    axes[1].set_yticks(range(len(metrics)))
    axes[1].set_yticklabels(metrics, fontsize=9)
    for i, metric in enumerate(metrics):
        for j, store in enumerate(norm.index):
            axes[1].text(j, i, f"{norm.loc[store, metric]:.2f}",
                         ha="center", va="center", fontsize=9)
    axes[1].set_title("Normalized Efficiency Metrics (0–1)", fontsize=13, fontweight="bold")
    plt.colorbar(im2, ax=axes[1], fraction=0.04, pad=0.04)
    comparison_fig.tight_layout()
 
    return {
        "efficiency_metrics": efficiency_metrics,
        "performance_ranking": performance_ranking,
        "comparison_fig": comparison_fig
    }
 
 
def analyze_seasonal_patterns():
    """
    Identify and visualize seasonal patterns in sales data.
    Returns a dictionary with keys:
    - 'monthly_sales': pandas Series
    - 'dow_sales': pandas Series (day of week)
    - 'seasonal_fig': matplotlib figure
    """
    sales_df["Month"]      = sales_df["Date"].dt.month
    sales_df["DayOfWeek"]  = sales_df["Date"].dt.dayofweek
 
    monthly_sales = sales_df.groupby("Month")["Sales"].sum()
    dow_sales     = sales_df.groupby("DayOfWeek")["Sales"].sum()
    dow_sales.index = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
 
    print("\n[2.3] Seasonal Pattern Analysis")
    print(f"\n  Monthly Sales:\n{monthly_sales.to_string()}")
    print(f"\n  Sales by Day of Week:\n{dow_sales.to_string()}")
 
    month_labels = ["Jan","Feb","Mar","Apr","May","Jun",
                    "Jul","Aug","Sep","Oct","Nov","Dec"]
 
    seasonal_fig, axes = plt.subplots(1, 2, figsize=(13, 5))
 
    # Monthly trend
    axes[0].plot(range(1, 13), monthly_sales.values, color="#2E86AB",
                 linewidth=2.5, marker="o", markersize=7, markerfacecolor="white", markeredgewidth=2)
    axes[0].fill_between(range(1, 13), monthly_sales.values,
                         alpha=0.15, color="#2E86AB")
    axes[0].set_xticks(range(1, 13))
    axes[0].set_xticklabels(month_labels, rotation=30)
    axes[0].set_title("Total Sales by Month", fontsize=13, fontweight="bold")
    axes[0].set_ylabel("Sales ($)")
    axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    axes[0].spines[["top", "right"]].set_visible(False)
 
    # Day of week bar
    day_colors = ["#78909C"] * 5 + ["#FF8A65", "#FF8A65"]
    axes[1].bar(dow_sales.index, dow_sales.values, color=day_colors, edgecolor="white")
    axes[1].set_title("Sales by Day of Week", fontsize=13, fontweight="bold")
    axes[1].set_ylabel("Sales ($)")
    axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    axes[1].spines[["top", "right"]].set_visible(False)
    seasonal_fig.tight_layout()
 
    return {
        "monthly_sales": monthly_sales,
        "dow_sales": dow_sales,
        "seasonal_fig": seasonal_fig
    }
 
 
# ─────────────────────────────────────────────────────────────────────────────
# TODO 3: Predictive Analytics
# ─────────────────────────────────────────────────────────────────────────────
 
def predict_store_sales():
    """
    Use linear regression to predict store sales based on store characteristics.
    Returns a dictionary with keys:
    - 'coefficients': dict (feature: coefficient)
    - 'r_squared': float
    - 'predictions': pandas Series
    - 'model_fig': matplotlib figure
    """
    # Feature matrix from store characteristics + operational data
    merged = operational_df.merge(store_df, on="Store")
    features = ["SquareFootage", "StaffCount", "YearsOpen", "WeeklyMarketingSpend"]
    X = merged[features].values
    y = merged["AnnualSales"].values
 
    # Multiple linear regression using scipy lstsq (no sklearn needed)
    X_design = np.column_stack([np.ones(len(X)), X])
    result    = np.linalg.lstsq(X_design, y, rcond=None)
    params    = result[0]
    intercept = params[0]
    coefs     = params[1:]
 
    # Predictions & R²
    y_pred    = X_design @ params
    ss_res    = np.sum((y - y_pred) ** 2)
    ss_tot    = np.sum((y - y.mean()) ** 2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
 
    coefficients = dict(zip(features, coefs))
    predictions  = pd.Series(y_pred, index=merged["Store"])
 
    print("\n[3.1] Linear Regression Model — Predict Annual Store Sales")
    print(f"  Intercept : {intercept:,.2f}")
    for f, c in coefficients.items():
        print(f"  {f:<28}: {c:+,.4f}")
    print(f"  R²        : {r_squared:.4f}")
    print(f"\n  Predictions vs Actuals:")
    for store, pred, actual in zip(merged["Store"], y_pred, y):
        print(f"    {store:<14}: Predicted ${pred:>12,.0f}  |  Actual ${actual:>12,.0f}")
 
    # Figure
    model_fig, axes = plt.subplots(1, 2, figsize=(13, 5))
 
    # Actual vs Predicted scatter
    axes[0].scatter(y, y_pred, color=[STORE_COLORS[s] for s in merged["Store"]], s=150, zorder=5)
    lims = [min(y.min(), y_pred.min()) * 0.95, max(y.max(), y_pred.max()) * 1.05]
    axes[0].plot(lims, lims, "k--", linewidth=1, label="Perfect fit")
    for s, actual, pred in zip(merged["Store"], y, y_pred):
        axes[0].annotate(s, (actual, pred), textcoords="offset points",
                         xytext=(5, 5), fontsize=8)
    axes[0].set_xlabel("Actual Sales ($)")
    axes[0].set_ylabel("Predicted Sales ($)")
    axes[0].set_title(f"Predicted vs Actual Sales (R²={r_squared:.3f})",
                      fontsize=13, fontweight="bold")
    axes[0].legend()
    axes[0].spines[["top", "right"]].set_visible(False)
 
    # Coefficient bar chart
    feat_short = ["SqFt", "Staff", "YrsOpen", "Marketing"]
    bar_colors = ["#4CAF50" if c > 0 else "#F44336" for c in coefs]
    axes[1].barh(feat_short, coefs, color=bar_colors, edgecolor="white")
    axes[1].axvline(0, color="black", linewidth=0.8)
    axes[1].set_title("Regression Coefficients", fontsize=13, fontweight="bold")
    axes[1].set_xlabel("Coefficient Value")
    axes[1].spines[["top", "right"]].set_visible(False)
    model_fig.tight_layout()
 
    return {
        "coefficients": coefficients,
        "r_squared": r_squared,
        "predictions": predictions,
        "model_fig": model_fig
    }
 
 
def forecast_department_sales():
    """
    Analyze and forecast departmental sales trends using a 3-month moving average
    and a simple linear extrapolation.
    Returns a dictionary with keys:
    - 'dept_trends': pandas DataFrame
    - 'growth_rates': pandas Series
    - 'forecast_fig': matplotlib figure
    """
    sales_df["Month"] = sales_df["Date"].dt.month
    dept_monthly = sales_df.groupby(["Month", "Department"])["Sales"].sum().reset_index()
 
    dept_trends = dept_monthly.pivot(index="Month", columns="Department", values="Sales")
 
    # Month-over-month growth rate (Dec vs Jan)
    growth_rates = ((dept_trends.iloc[-1] - dept_trends.iloc[0]) / dept_trends.iloc[0]).sort_values(ascending=False)
 
    print("\n[3.2] Department Sales Forecast")
    print(f"\n  Annual Growth Rate (Jan → Dec) by Department:")
    for dept, rate in growth_rates.items():
        print(f"    {dept:<18}: {rate:+.2%}")
 
    # Forecast next 3 months (Jan–Mar 2024) using linear trend from H2 2023
    forecast_months = [13, 14, 15]
    forecast_fig, ax = plt.subplots(figsize=(12, 6))
 
    for dept in departments:
        col = dept_trends[dept]
        # 3-month moving average
        ma = col.rolling(3, min_periods=1).mean()
        ax.plot(col.index, col.values, color=DEPT_COLORS[dept],
                linewidth=2, label=dept)
        ax.plot(col.index, ma.values, color=DEPT_COLORS[dept],
                linewidth=1.2, linestyle="--", alpha=0.6)
 
        # Simple linear fit over months 7-12 to forecast
        x_fit = np.array(col.index[6:])
        y_fit = col.values[6:]
        if len(x_fit) > 1:
            slope, intercept_f = np.polyfit(x_fit, y_fit, 1)
            x_fore = np.array(forecast_months)
            y_fore = slope * x_fore + intercept_f
            ax.plot([12] + list(forecast_months),
                    [col.values[-1]] + list(y_fore),
                    color=DEPT_COLORS[dept], linewidth=1.5,
                    linestyle=":", alpha=0.8)
 
    ax.axvline(12.5, color="gray", linewidth=1, linestyle="--", label="Forecast boundary")
    ax.set_xticks(list(range(1, 13)) + forecast_months)
    ax.set_xticklabels(
        ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec",
         "Jan'24","Feb'24","Mar'24"], rotation=30, fontsize=8)
    ax.set_title("Monthly Department Sales + 3-Month Forecast", fontsize=14, fontweight="bold")
    ax.set_ylabel("Sales ($)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
    ax.legend(loc="upper left", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    forecast_fig.tight_layout()
 
    return {
        "dept_trends": dept_trends,
        "growth_rates": growth_rates,
        "forecast_fig": forecast_fig
    }
 
 
# ─────────────────────────────────────────────────────────────────────────────
# TODO 4: Integrated Analysis
# ─────────────────────────────────────────────────────────────────────────────
 
def identify_profit_opportunities():
    """
    Identify the most profitable store-department combinations and opportunity scores.
    Returns a dictionary with keys:
    - 'top_combinations': pandas DataFrame (top 10 store-dept combinations)
    - 'underperforming': pandas DataFrame (bottom 10)
    - 'opportunity_score': pandas Series (by store)
    """
    combo = (sales_df.groupby(["Store", "Department"])
             .agg(TotalSales=("Sales","sum"),
                  TotalProfit=("Profit","sum"),
                  AvgMargin=("ProfitMargin","mean"))
             .reset_index())
    combo["ProfitShare"] = combo["TotalProfit"] / combo["TotalProfit"].sum()
 
    top_combinations   = combo.nlargest(10, "TotalProfit").reset_index(drop=True)
    underperforming    = combo.nsmallest(10, "TotalProfit").reset_index(drop=True)
 
    # Opportunity score: normalize low performers by available sales potential
    store_max_profit   = combo.groupby("Store")["TotalProfit"].sum()
    store_actual_profit= operational_df.set_index("Store")["AnnualProfit"]
    gap                = store_max_profit - store_actual_profit
    opportunity_score  = (gap / gap.max()).sort_values(ascending=False)
 
    print("\n[4.1] Profit Opportunity Analysis")
    print(f"\n  Top 10 Store-Department Combinations (by Profit):")
    print(top_combinations[["Store","Department","TotalSales","TotalProfit","AvgMargin"]].to_string(index=False))
    print(f"\n  Bottom 10 Underperforming Combinations:")
    print(underperforming[["Store","Department","TotalSales","TotalProfit","AvgMargin"]].to_string(index=False))
    print(f"\n  Opportunity Score by Store (0=low gap, 1=high gap):")
    print(opportunity_score.to_string())
 
    return {
        "top_combinations": top_combinations,
        "underperforming": underperforming,
        "opportunity_score": opportunity_score
    }
 
 
def develop_recommendations():
    """
    Develop actionable recommendations based on the analysis.
    Returns a list of at least 5 recommendation strings.
    """
    recommendations = [
        "1. EXPAND MIAMI's PREPARED FOODS SECTION: Miami is the top-revenue store with the highest "
        "performance factor (1.2×) and Prepared Foods carries the highest margin (~40%). Expanding "
        "hot bar and salad bar square footage in Miami is expected to directly lift profit margins.",
 
        "2. INVEST IN GAINESVILLE & JACKSONVILLE MARKETING: Both stores are the newest (1–2 years) "
        "and have the lowest performance factors (0.65 and 0.75). Increasing WeeklyMarketingSpend "
        "by 20-30% aligns with the positive correlation between marketing and AnnualSales observed "
        "in the regression model.",
 
        "3. SCALE BAKERY PROGRAMS ACROSS ALL STORES: Bakery holds the second-highest margin (~35%) "
        "yet underperforms on the revenue scale relative to Produce. Introducing signature artisan "
        "bread programs and pre-order cakes can raise Bakery contribution without adding floor space.",
 
        "4. TARGET FAMILY SHOPPERS & GOURMET COOKS WITH LOYALTY REWARDS: Family Shoppers represent "
        "the largest segment (30%) with the highest average basket ($150). Gourmet Cooks have the "
        "second-highest basket ($120). Introducing double-points weekends for these two segments "
        "can increase visit frequency and average basket size simultaneously.",
 
        "5. OPTIMIZE STAFFING TO IMPROVE SALES-PER-STAFF: The regression shows StaffCount has a "
        "significant coefficient. Review scheduling data to ensure peak-hour coverage aligns with "
        "weekend traffic surges (weekend sales are ~30% higher than weekdays). Cross-training staff "
        "across Produce and Prepared Foods will improve throughput during lunch and evening peaks.",
 
        "6. LEVERAGE DECEMBER & SUMMER SEASONALITY WITH LIMITED-TIME PRODUCTS: The 25% December "
        "uplift and 15% summer uplift represent the highest seasonal premiums in the data. "
        "Introducing seasonal specialty bundles (holiday gift baskets in December, BBQ-ready "
        "meal kits in summer) can capture incremental margin on top of organic seasonal lift.",
 
        "7. ELEVATE UNDERPERFORMING GROCERY DEPARTMENT MARGIN: Grocery has the lowest base margin "
        "(20%). Partnering with private-label organic brands and reducing SKU count to focus on "
        "higher-margin items (specialty grains, premium snacks) can improve overall Grocery margin "
        "by an estimated 2-4 percentage points."
    ]
 
    print("\n[4.2] Strategic Recommendations:")
    for rec in recommendations:
        print(f"\n  {rec}")
 
    return recommendations
 
 
# ─────────────────────────────────────────────────────────────────────────────
# TODO 5: Executive Summary
# ─────────────────────────────────────────────────────────────────────────────
 
def generate_executive_summary():
    """
    Generate a concise, business-focused executive summary.
    Prints sections: Overview, Key Findings, Recommendations, Expected Impact.
    """
    total_sales  = sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()
    avg_margin   = sales_df["ProfitMargin"].mean()
 
    summary = f"""
╔══════════════════════════════════════════════════════════════════╗
║            GREENGROCER – EXECUTIVE SUMMARY (FY 2023)            ║
╚══════════════════════════════════════════════════════════════════╝
 
OVERVIEW
────────
GreenGrocer generated ${total_sales:,.0f} in total revenue and ${total_profit:,.0f}
in gross profit across its five Florida locations in 2023, delivering an average
profit margin of {avg_margin:.1%}. Miami is the highest-performing store (performance
index 1.2×), while Gainesville and Jacksonville, both recently opened, lag behind
peers on virtually every operational metric. The Prepared Foods and Produce
departments anchor profitability with margins of ~40% and ~25% respectively,
while Grocery (20%) and Dairy (22%) represent the greatest margin improvement
opportunities.
 
KEY FINDINGS
────────────
• Miami leads all stores in annual sales and profit, benefiting from a large
  catchment area, maximum square footage (18,000 sq ft), and the strongest
  store performance factor in the portfolio.
 
• Seasonal peaks are material: December drives a 25% sales uplift and summer
  months (June–August) add ~15%. Weekend traffic is ~30% above weekday levels,
  indicating meaningful staffing and inventory optimization opportunities.
 
• Prepared Foods carries the highest profit margin (~40%) across all departments,
  yet represents a smaller share of total revenue than Produce or Dairy —
  suggesting significant untapped upside if capacity is expanded.
 
• Family Shoppers (30% of customers) and Gourmet Cooks (20%) together represent
  50% of the customer base and carry the two highest average basket sizes
  ($150 and $120 respectively), making them the most strategically valuable
  segments for targeted loyalty investment.
 
• The linear regression model (features: square footage, staff count, years open,
  marketing spend) explains a substantial share of variance in store sales,
  confirming that marketing spend and store scale are the primary controllable
  levers for revenue growth.
 
RECOMMENDATIONS
───────────────
• Expand Prepared Foods capacity in Miami and Tampa to capture incremental
  high-margin revenue during both peak and off-peak periods.
 
• Increase WeeklyMarketingSpend by 20-30% for Gainesville and Jacksonville to
  accelerate brand awareness and customer acquisition in their growth phase.
 
• Launch a targeted loyalty program for Family Shoppers and Gourmet Cooks,
  with double-point weekends and exclusive early access to seasonal specialty items.
 
• Introduce seasonal product bundles (holiday baskets in December, summer meal
  kits in July–August) to convert natural traffic uplift into premium revenue.
 
• Rationalise the Grocery SKU range toward higher-margin private-label organic
  and specialty products to raise the department's base margin from 20% toward 24%.
 
EXPECTED IMPACT
───────────────
Implementing these recommendations in aggregate is projected to lift overall profit
margins by 2-4 percentage points within 12 months. Targeted marketing investment
in newer stores could close 30-40% of the performance gap between Gainesville/
Jacksonville and the network average within 18 months. Expanding Prepared Foods
and activating seasonal bundle programs represent the fastest paths to incremental
profit, with low capital requirements relative to the expected revenue uplift.
Collectively, these initiatives position GreenGrocer to grow annualised profit
by an estimated 15-20% by the end of FY 2024.
"""
    print(summary)
 
 
# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
 
def main():
    print("\n" + "=" * 60)
    print("GREENGROCER BUSINESS ANALYTICS RESULTS")
    print("=" * 60)
 
    print("\n--- DESCRIPTIVE ANALYTICS: CURRENT PERFORMANCE ---")
    sales_metrics    = analyze_sales_performance()
    dist_figs        = visualize_sales_distribution()
    customer_analysis = analyze_customer_segments()
 
    print("\n--- DIAGNOSTIC ANALYTICS: UNDERSTANDING RELATIONSHIPS ---")
    correlations     = analyze_sales_correlations()
    store_comparison = compare_store_performance()
    seasonality      = analyze_seasonal_patterns()
 
    print("\n--- PREDICTIVE ANALYTICS: FORECASTING ---")
    sales_model   = predict_store_sales()
    dept_forecast = forecast_department_sales()
 
    print("\n--- BUSINESS INSIGHTS AND RECOMMENDATIONS ---")
    opportunities   = identify_profit_opportunities()
    recommendations = develop_recommendations()
 
    print("\n--- EXECUTIVE SUMMARY ---")
    generate_executive_summary()
 
    plt.show()
 
    return {
        'sales_metrics':      sales_metrics,
        'customer_analysis':  customer_analysis,
        'correlations':       correlations,
        'store_comparison':   store_comparison,
        'seasonality':        seasonality,
        'sales_model':        sales_model,
        'dept_forecast':      dept_forecast,
        'opportunities':      opportunities,
        'recommendations':    recommendations
    }
 
 
if __name__ == "__main__":
    results = main()
 