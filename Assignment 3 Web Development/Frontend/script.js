// Get references to DOM elements
const form = document.getElementById('jobApplicationForm');
const modal = document.getElementById('modal');
const submittedDataContainer = document.getElementById('submittedData');
const closeModalButton = document.getElementById('closeModal');
const saveDataButton = document.getElementById('saveData');

// Function to show modal with submitted data
function showModal(data) {
    // Clear previous data
    submittedDataContainer.innerHTML = '';

    // Iterate over form data and display in modal
    for (const [key, value] of Object.entries(data)) {
        const row = document.createElement('div');
        row.classList.add('flex', 'justify-between', 'mb-2');
        
        const label = document.createElement('div');
        label.textContent = `${key}:`;
        label.classList.add('font-bold');
        
        const text = document.createElement('div');
        text.textContent = Array.isArray(value) ? value.join(', ') : value;
        
        row.appendChild(label);
        row.appendChild(text);
        submittedDataContainer.appendChild(row);
    }

    // Show modal
    modal.classList.remove('hidden');
}

// Event listener for form submission
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get form data
    const formData = new FormData(form);
    const data = {};

    // Iterate over form data and handle multiple checkboxes
    for (const [key, value] of formData.entries()) {
        if (data[key]) {
            // If the key already exists in data (multiple checkboxes), append the value to an array
            if (!Array.isArray(data[key])) {
                data[key] = [data[key]]; // Convert to array if it's not already an array
            }
            data[key].push(value);
        } else {
            // If it's the first occurrence of the key, initialize it as a single value or array
            data[key] = value;
        }
    }

    // Show modal with submitted data
    showModal(data);
});

// Event listener for closing modal
closeModalButton.addEventListener('click', function() {
    modal.classList.add('hidden'); // Hide modal
});

// Event listener for saving data
saveDataButton.addEventListener('click', function() {
    const formData = new FormData(form);
    fetch('http://127.0.0.1:5000/save_data', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Data saved successfully:', data);
        alert('Data saved successfully!');
    })
    .catch(error => {
        console.error('There was a problem saving the data:', error);
        alert('There was a problem saving the data. Please try again.');
    });
});
