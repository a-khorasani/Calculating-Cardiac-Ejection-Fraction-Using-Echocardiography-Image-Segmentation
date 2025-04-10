document.addEventListener('DOMContentLoaded', function() {
    const fileUpload = document.getElementById('file-upload');
    const fileUploadLabel = document.querySelector('.file-upload-label');
    const selectedFilesContainer = document.createElement('div');
    selectedFilesContainer.className = 'selected-files';
    fileUploadLabel.parentNode.insertBefore(selectedFilesContainer, fileUploadLabel.nextSibling);

    fileUpload.addEventListener('change', function() {
        selectedFilesContainer.innerHTML = '';
        
        if (this.files.length > 0) {
            Array.from(this.files).forEach((file, index) => {
                const fileElement = document.createElement('div');
                fileElement.className = 'selected-file';
                fileElement.innerHTML = `
                    <span>${file.name}</span>
                    <span class="remove-file" data-index="${index}">
                        <i class="fas fa-times"></i>
                    </span>
                `;
                selectedFilesContainer.appendChild(fileElement);
            });
            
            const countElement = document.createElement('div');
            countElement.className = 'file-count';
            countElement.style.marginTop = '10px';
            countElement.style.fontSize = '0.9rem';
            countElement.style.color = '#666';
            countElement.textContent = `Number of selected files ${this.files.length}`;
            selectedFilesContainer.appendChild(countElement);
        }
    });

    selectedFilesContainer.addEventListener('click', function(e) {
        if (e.target.closest('.remove-file')) {
            const index = e.target.closest('.remove-file').getAttribute('data-index');
            const files = Array.from(fileUpload.files);
            files.splice(index, 1);
            
            const dataTransfer = new DataTransfer();
            files.forEach(file => dataTransfer.items.add(file));
            fileUpload.files = dataTransfer.files;
            
            const event = new Event('change');
            fileUpload.dispatchEvent(event);
        }
    });

    fileUploadLabel.addEventListener('dragover', function(e) {
        e.preventDefault();
        this.classList.add('drag-over');
    });

    fileUploadLabel.addEventListener('dragleave', function() {
        this.classList.remove('drag-over');
    });

    fileUploadLabel.addEventListener('drop', function(e) {
        e.preventDefault();
        this.classList.remove('drag-over');
        
        if (e.dataTransfer.files.length) {
            fileUpload.files = e.dataTransfer.files;
            const event = new Event('change');
            fileUpload.dispatchEvent(event);
        }
    });
});