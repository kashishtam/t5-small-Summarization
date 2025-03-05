async function summarizeArticle() {
    const articleInput = document.getElementById("articleInput").value;
    const summaryOutput = document.getElementById("summaryOutput");

    // Clear previous output
    summaryOutput.innerHTML = "";
    summaryOutput.classList.remove("error");

    // Show spinner
    summaryOutput.innerHTML = '<i class="fas fa-spinner spinner"></i>';
    summaryOutput.classList.remove("error");
    
    try {
        const response = await fetch("http://localhost:5001/summarize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ article: articleInput })
        });

        const data = await response.json();

        if (response.ok) {
            summaryOutput.textContent = data.summary;
        } else {
            summaryOutput.textContent = data.error || "An error occurred.";
            summaryOutput.classList.add("error");
        }
    } catch (error) {
        summaryOutput.textContent = "Failed to connect to the API: " + error.message;
        summaryOutput.classList.add("error");
    }
}

function clearArticle() {
    const articleInput = document.getElementById("articleInput");
    //const summaryOutput = document.getElementById("summaryOutput");
    articleInput.value = "";  // Clear article input
    //summaryOutput.textContent = "";  // Clear summary output
}