from django.http import HttpResponse

def task_create(request):
    html_reponse = """
        <style>
        
        
        h1 {
            text-align: center;
            color: blue;
            background-color: beige;
        }
        
        
        form {
            width: 15%;
            margin: 0 auto;
            padding: 40px;
        }
        
        
        label {
            font-weight: bold; 
        }
        
        
        button {
            padding: 10px 20px;
            background-color: blue;
            color: white;
            border: none;
            
        }
        </style>
        
        
        <h1>Yangi vazifa yaratish</h1>
        
        
        <form>
            <label>Vazifa nomi:</label>
            <input type="text">
            
            <br> <br>
            
            <label>Tavsif:</label>
            <textarea>
            
            </textarea>
            
            <br> <br>
            
            <label>Muddati:</label>
            <input type="date">
            
            <br> <br>
            
            <label>Muhimlik darajasi:</label>
            
                <select>
                    <option>Past</option>
                    <option>O'rta</option>
                    <option>Yuqori</option>
                </select>
                
            <br> <br>   
            
            <button type="submit">Vazifani saqlash</button>
                
        </form>
    """
    return HttpResponse(html_reponse)
