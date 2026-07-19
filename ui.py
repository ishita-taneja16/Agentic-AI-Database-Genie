import streamlit as st
import pandas as pd
import sqlite3
from ai_query import generate_sql

# 🔥 Page config
st.set_page_config(page_title="AI Database Genie", layout="wide")

# 🎨 Custom styling (dark + clean UI)
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}
.big-title {
    font-size: 40px;
    font-weight: bold;
}
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# 🔥 Header
st.markdown('<div class="big-title">🤖 AI Database Genie Dashboard</div>', unsafe_allow_html=True)

# Input
question = st.text_input("Ask your data")

# DB function
def run_query(sql):
    conn = sqlite3.connect("houses.db")
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

# MAIN LOGIC
if question:
    st.markdown(f"**🧑 You:** {question}")

    sql = generate_sql(question)

    st.subheader("Generated SQL:")
    st.code(sql)

    try:
        df = run_query(sql)

        st.markdown("**🤖 Genie:** Here’s what I found 👇")

        # 🔥 If single value result (like MAX/MIN)
        if df.shape[1] == 1:
            value = df.iloc[0, 0]

            st.markdown(f"""
            <div class="card">
                <h2>📊 Result</h2>
                <h1 style="color:#22c55e;">₹ {int(value):,}</h1>
            </div>
            """, unsafe_allow_html=True)

        else:
            # 🔥 Layout split
            col1, col2 = st.columns([2, 1])

            with col1:
                st.subheader("📋 Data")
                st.dataframe(df)

            with col2:
                if "price" in df.columns:
                    st.subheader("📊 Insights")

                    st.metric("Max Price", int(df["price"].max()))
                    st.metric("Min Price", int(df["price"].min()))
                    st.metric("Avg Price", int(df["price"].mean()))

        # 🔥 Chart section
        if "price" in df.columns and "location" in df.columns:
            st.subheader("📊 Price by Location")

            chart_df = df.groupby("location")["price"].mean().reset_index()

            st.bar_chart(chart_df, x="location", y="price")

    except Exception as e:
        st.error("Error in query execution")
        st.write(e)

# Suggestions
st.markdown("💡 Try: highest price in Mohali, 3 bedroom houses in Delhi")