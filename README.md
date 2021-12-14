# statistics-service
Best statistics service


**Регистрация**
----

* **URL**

  /api/register/
  

* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `username=[string]`
   `password=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'username' : 'string', 'password' : "hash[password]" }`
    

**Авторизация**
----

* **URL**

  /api/login/

* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `username=[string]`
   `password=[string]`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'refresh' : 'string', 'access' : "string" }`
    
**Используйте ключ 'access' для авторизации**


**Просмотр статистики**
----

* **URL**

  /statistic/save/
  

* **Method:**

  `POST`
  
*  **Параметры**

   **Обязательно:**
 
   `date=[YYYY:MM:DD]`
   **Опционально:**
 
   `views=[int]`
   `clicks=[int]`
   `cost=[decimal]`
 

* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'id' : 'int', 'date' : "datetime". 'views' : 'int', 'clicks' : 'int', 'cost' : 'decimal', 'cpc' : 'decimal', 'cpm' : 'decimal' }`
    
 **Просмотр cтатистики**
----

* **URL**

  /statistic/view/
  

* **Method:**

  `GET`
  
*  **Параметры**

   **Обязательно:**
 
   `None`
   
   **Опционально:**
 
   `order = model field`
   
   order - параметр для сортировки по конкретному полю
 

* **Ответ**

  * **Code:** 200 <br />
    **Content:** `{ 'id' : 'int', 'date' : "datetime". 'views' : 'int', 'clicks' : 'int', 'cost' : 'decimal', 'cpc' : 'decimal', 'cpm' : 'decimal' }`
    
 **Удаление  статистики**
----

* **URL**

  /api/statistic/delete/pk/
  
  pk - номер статистики

* **Method:**

  `DELETE`
  
*  **Параметры**

   **Обязательно:**
 
   `NONE`


* **Ответ**

  * **Code:** 200 <br />
    **Content:** `None`

    
    
