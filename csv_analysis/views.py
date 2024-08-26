import os
import re
import matplotlib
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CSVFileForm
from .models import CSVFile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def upload_file(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('analyze_file', file_id=form.instance.id)
    else:
        form = CSVFileForm()
    return render(request, 'csv_analysis/upload.html', {'form': form})


# Set the Matplotlib backend to 'Agg'
matplotlib.use('Agg')

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_]', '_', filename)

def analyze_file(request, file_id):
    csv_file = CSVFile.objects.get(id=file_id)
    df = pd.read_csv(csv_file.file.path)

    # Basic Data Analysis
    head = df.head()
    description = df.describe()
    missing_values = df.isnull().sum().to_frame('missing_values')

    # Handle Missing Values
    if request.method == 'POST':
        handle_missing = request.POST.get('handle_missing')
        if handle_missing == 'drop':
            df = df.dropna()
        elif handle_missing == 'fill_mean':
            df = df.fillna(df.mean())
        elif handle_missing == 'fill_median':
            df = df.fillna(df.median())
        elif handle_missing == 'ffill':
            df = df.fillna(method='ffill')
        elif handle_missing == 'bfill':
            df = df.fillna(method='bfill')
        
        # Update data after handling missing values
        head = df.head()
        description = df.describe()
        missing_values = df.isnull().sum().to_frame('missing_values')

    # Data Visualization
    histograms = []
    for column in df.select_dtypes(include=['number']).columns:
        plt.figure()
        sns.histplot(df[column].dropna(), kde=False)
        sanitized_column = sanitize_filename(column)
        plot_dir = os.path.join(settings.STATIC_ROOT, 'histograms')
        if not os.path.exists(plot_dir):
            os.makedirs(plot_dir)
        plot_path = os.path.join(plot_dir, f'hist_{sanitized_column}.png')
        plt.savefig(plot_path)
        histograms.append(f'histograms/hist_{sanitized_column}.png')
        plt.close()

    context = {
        'head': head.to_html(),
        'description': description.to_html(),
        'missing_values': missing_values.to_html(),
        'histograms': histograms,
    }
    return render(request, 'csv_analysis/analyze.html', context)
