# SurveyFlow

SurveyFlow is a visual tool for analyzing encoded survey responses using interactive flow charts. It helps you quickly answer complex logic questions like:

> "How many people answered `0` to Q1, `4` to Q5, and `2` to Q9?"

...without writing a single COUNTIF.

---

## 🔍 What It Does

- ✅ Reads a dataset with encoded responses
- ✅ Splits the response string into individual question columns (Q1–Q9)
- ✅ Lets you build a question path using dropdowns
- ✅ Generates a **visual flow chart** showing respondent counts at each step
- ✅ Optionally shows the matching data table

---

## 📦 Example

Say you want to find how many respondents:
- Said `0` to Q1
- And `4` to Q5
- And `2` to Q9

You'll get a flow like:

Start [432 total]
└── Q1 = 0 [158]
└── Q5 = 4 [54]
└── Q9 = 2 [12]
