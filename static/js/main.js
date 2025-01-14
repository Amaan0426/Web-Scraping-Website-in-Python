document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM content loaded');

    const scrapeForm = document.querySelector('#scrape-form');
    const resultContainer = document.querySelector('#result-container');

    if (scrapeForm) {
        scrapeForm.addEventListener('submit', function (event) {
            event.preventDefault();

            const url = document.querySelector('#url-input').value;
            console.log('URL:', url);

            fetch('/scrape', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: url }),
            })
            .then(response => {
                console.log('Response Status:', response.status); // Add this line
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Data from server:', data);
                if (data.error) {
                    alert(`Error: ${data.error}`);
                } else {
                    displayScrapedData(data.data);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    function displayScrapedData(data) {
        resultContainer.innerHTML = ''; // Clear previous results
    
        if (!Array.isArray(data) || data.length === 0) {
            resultContainer.innerHTML = '<p>No data available.</p>';
            return;
        }
    
        const table = document.createElement('table');
        const thead = document.createElement('thead');
        const tbody = document.createElement('tbody');
    
        // Create table header
        const headerRow = document.createElement('tr');
        Object.keys(data[0] || {}).forEach(key => {
            const th = document.createElement('th');
            th.textContent = key;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);
    
        // Create table rows with data
        data.forEach(item => {
            if (typeof item !== 'object' || item === null) {
                console.error('Invalid data format:', item);
                return;
            }
    
            const row = document.createElement('tr');
            Object.values(item).forEach(value => {
                const td = document.createElement('td');
                td.textContent = value;
                row.appendChild(td);
            });
            tbody.appendChild(row);
        });
        table.appendChild(tbody);
    
        resultContainer.appendChild(table);
    }
        
});
