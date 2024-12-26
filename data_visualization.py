import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_gpa_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['GPA'], bins=20, kde=True)
    plt.title('GPA Distribution')
    plt.xlabel('GPA')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

def plot_attendance_by_gender(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Gender', y='Attendance', data=df)
    plt.title('Attendance by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Attendance Percentage')
    plt.grid()
    plt.show()
