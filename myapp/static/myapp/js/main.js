// Main JavaScript file

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');
    
    // Add event listeners to all items in the list
    const items = document.querySelectorAll('.item-list li');
    items.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#e9e9e9';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '#f9f9f9';
        });
    });
    
    // Add a simple confirmation for delete actions
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
});