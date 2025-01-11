/**
 * The script of the app in javascript.
 * @author RIT GDSC.
 * @contributor Huy Le
 */
// Wait for the DOM to fully load before executing the script
document.addEventListener('DOMContentLoaded', function() {
    // Select the form element by its ID
    const form = document.getElementById('cropForm');

    // Add an event listener to the form to handle the submit event
    form.addEventListener('submit', function(event) {
        // Retrieve the values from the input fields and convert them to floats
        const pH = parseFloat(document.getElementById('pH').value);
        const moisture = parseFloat(document.getElementById('moisture').value);
        const nutrients = parseFloat(document.getElementById('nutrients').value);

        // Check if any of the input values are not numbers (NaN)
        if (isNaN(pH) || isNaN(moisture) || isNaN(nutrients)) {
            // Display an alert message to the user
            alert('Please enter valid numbers for all fields.');
            // Prevent the form from being submitted
            event.preventDefault();
        }
    });
});