import streamlit as st
from utils.google_sheet import add_expense

# -------------------------------------
# Page Configuration
# -------------------------------------
st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="centered"
)

# -------------------------------------
# Title
# -------------------------------------
st.title("💰 Expense Tracker")
st.write("Track your daily expenses effortlessly.")

st.divider()

# -------------------------------------
# Form
# -------------------------------------
with st.form("expense_form", clear_on_submit=True):

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        step=1.0,
        format="%.2f"
    )

    description = st.text_input(
        "Description",
        placeholder="Example: Lunch, Petrol, Shopping..."
    )

    submitted = st.form_submit_button("➕ Add Expense")

# -------------------------------------
# Save Expense
# -------------------------------------
if submitted:

    # Validation
    if amount <= 0:
        st.warning("Please enter a valid amount.")

    elif not description.strip():
        st.warning("Please enter a description.")

    else:

        try:

            with st.spinner("Saving expense..."):

                add_expense(amount, description)

            st.success("Expense saved successfully ✅")

            st.balloons()

        except Exception as e:

            import traceback

            st.error("Something went wrong ❌")

            st.code(traceback.format_exc())
