{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ee654d02-87ca-4efe-9be0-5e83e7fa4c71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model trained and saved successfully!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.linear_model import LinearRegression\n",
    "import pickle\n",
    "\n",
    "# Sample dataset (you can replace with real data)\n",
    "data = {\n",
    "    \"temperature\": [25, 30, 35, 20, 28],\n",
    "    \"humidity\": [60, 55, 40, 70, 65],\n",
    "    \"prev_aqi\": [80, 120, 150, 60, 100],\n",
    "    \"aqi\": [90, 130, 180, 70, 110]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Features and target\n",
    "X = df[[\"temperature\", \"humidity\", \"prev_aqi\"]]\n",
    "y = df[\"aqi\"]\n",
    "\n",
    "# Train model\n",
    "model = LinearRegression()\n",
    "model.fit(X, y)\n",
    "\n",
    "# Save model\n",
    "with open(\"aqi_model.pkl\", \"wb\") as f:\n",
    "    pickle.dump(model, f)\n",
    "\n",
    "print(\"Model trained and saved successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5833dbc7-02be-4d74-b56e-5aca159d2d48",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
