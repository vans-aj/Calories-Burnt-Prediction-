function predictCalories() {
    const weight = parseFloat(document.getElementById('weight').value);
    const duration = parseFloat(document.getElementById('duration').value);
    if (!isNaN(weight) && !isNaN(duration)) {
        const result = (weight * duration) / 10;  // Placeholder calculation
        document.getElementById('result').innerText = `Estimated Calories Burnt: ${result.toFixed(2)} kcal`;
    } else {
        document.getElementById('result').innerText = "Please enter valid inputs.";
    }
}
