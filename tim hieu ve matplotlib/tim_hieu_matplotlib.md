# Một số thành phần cơ bản có trong biểu đồ.
- `legend((line1,line2,line3),('label1','label2','label3'))`: tạo chú giải cho biểu đồ line1,line2,line3.
- `xlabel('text')`: tạo ra tên cho trục x
- `ylabel('text')`: tạo ra tên cho trục y
- `xticks(x,a)`: thay đổi tên các tọa độ của xi trong x ứng với ai có trong a theo trục tọa độ x
- `yticks(y,b)`: thay đổi tên các tọa độ của yi trong y ứng với ai có trong a theo trục tọa độ y
- `title('content')`: tạo tên biểu đồ
- `ylim(ymin,ymax)`: tạo ra giới hạn cho trục tọa độ y với ymin và ymax vd: `plt.ylim(0,120)`
- `xlim(xmin,xmax)`: tạo ra giới hạn cho trục tọa độ x với xmin và xman vd: `plt.xlim(0,20)`
....
 ## a. line chart
Biểu đồ line có nhiều thuộc tính, nó có thể là: linewidth(độ dày), dash style(loại đường), antialiased...
 để tạo 1 biểu đồ line, ta dùng câu lệnh đơn giản: `plt.plot(x,y)`  trong đó x là tọa độ trục x, y là tọa độ trục y.  
ví dụ sau đây định nghĩa một số thuộc tính hay sử dụng củ biểu đồ  line.
```c        
    import matplotlib.pyplot as plt
    x=[1,2,3,4,5]
    y=[1,2,3,4,5]
    plt.plot(x,y,ls='--',color='red',alpha=0.5,linewidth=2.0, label='do thi x,y')
    plt.xlabel('toa do x')
    plt.ylabel('toa do y')
    plt.title('do thi line')
    plt.legend()
    plt.show()
```
    - với ví dụ trên sẽ tạo ra biểu đồ với độ dày của đường kẻ là linewidth=2.0 lớn hơn so với mặc định, và loại đường của biểu đồ là đường nét đứt được định dạng bởi thuộc tính ls= '--', thay vì mặc định là đường nét liền, màu của đường kẻ được định dạng bởi thuộc tính color='red' thay vì mặc định là màu 'blue', và alpha=0.5 là độ đậm nhạt của đường kẻ.
    - plt.xlabel(): tạo tiêu đề cho tọa độ x
    - plt.ylabel(): tạo tiêu đề cho tọa độ y    
    - label (bên trong plt.plot()): tạo ghi chú cho đường đó.
    - plt.title('do thi line'): được sử dụng để đặt tên cho đồ thị.
    
Với câu lệnh ở ví dụ trên, thay vì viết các thuộc tính trong hàm `plt.plot()`, ta có thể dùng hàm `setp()` để chứa các thuộc tính đó.
```c
   import matplotlib.pyplot as plt
   x=[1,2,3,4,5]
   y=[1,2,3,4,5]
   lines= plt.plot(x,y) 
   plt.setp(lines,ls='--',color='red',alpha=0.5,linewidth=2.0)
   plt.show()
``` 
Kết quả thực hiện các câu lệnh trên:
<image src="../tim hieu ve matplotlib/figure1.png">

## Ngoài các thuộc tính cơ bản hay sử dụng trên, line còn có các thuộc tính như: 
    + marker: dùng để đánh dấu các điểm giao giữa hai tọa độ. các giá trị có thể gán như: '+', ',','.','1','2','o','s',.....
    + markeredgecolor: màu đường viền của marker
    + markersize: kích thước của marker.  

Ngoài ra trong một biểu đồ có thể có nhiều đường như sau: 
```h
    import matplotlib.pyplot as plt
    x=[1,2,3,4,5,6,7,8]
    y=[1,2,3,4,5,9,11,15]
    x1=[1,2,5,7,9,11]
    y1=[2,4,6,1,7,2]
    plt.plot(x,y,ls='--',color='red',marker='o',markersize=10,linewidth=2.0, label='do thi x,y')
    plt.plot(x1,y1,ls='-',color='green',marker='*',markersize=10,linewidth=2.0, label='do thi x1,y1')
    plt.xlabel('toa do x')
    plt.ylabel('toa do y')
    plt.title('do thi line')
    plt.legend()
    plt.show()
```
Kết quả: 
<image src="../tim hieu ve matplotlib/vidu1.jpg">

## b. bar chart( biểu đồ bar )
Để tạo ra một biểu đồ bar ta sử dụng câu lệnh: 
`plt.bar(left, height,width=0.8)`
- trong đó:  
    + `left`: là các tọa độ x của bar  
    + `height`: chiều cao của các cột bar  
    + `width`: độ dày của cột bar (mặc định là 0.8)  
- ngoài các thuộc tính trên ta còn có như:   
    + `bottom`: khoảng cách giữa các cột với trục tọa độ x 
    + `color`: màu sắc  
    +`edgecolor`:màu sắc đường viền của bar  
    + `linewidth`: độ dày của cạnh  
    + `align`:căn chỉnh    

Ví dụ về tạo một biểu đồ bar đơn giản về tuổi thọ trung bình của các nước: 
```c
import matplotlib.pyplot as plt
import numpy as np
obj=('Viet Nam','Thai Lan','Trung Quoc','Nhat Ban','Han Quoc')
y=[70,75,80,85,90]
ind =np.arange(len(obj))
plt.bar(ind,y, width=0.4,linewidth=1,align='center',alpha=1,  color='green',bottom=1, label='Do tuoi trung binh cac nuoc')
plt.xlabel('Country', fontsize=20)i90
plt.ylabel('Age', fontsize=20)
plt.title('DO tuoi trung binh cua cac nuoc')
plt.xticks(ind,obj)
plt.grid(True)
plt.legend()
plt.show()
```
Kết quả: 
<image src="../tim hieu ve matplotlib/dotuoi.png">
- np.arange(len(obj)): được dùng để lấy chỉ số của mảng obj
- plt.grid(True): dùng để tạo các dòng kẻ mờ trên biểu đồ.
plt.xticks(ind,obj): được dùng để thay các tọa độ trên trục x(như hình vẽ).
- các câu lệnh còn lại đã được giải thích ở trên biểu đồ line.

## Để hiểu rõ hơn về biểu đồ, ta có ví dụ sau: 
```h
import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
y=[70,75,80,85,90]
z=[42,54,87,56,75]
t=[43,65,32,87,90]
ind =np.arange(len(x))
color=['red','green','blue']
width=0.2
plt.bar(ind,y, width=width,align='center',alpha=1,  color=color[0],label='toa do y')
plt.bar(ind + width,z, width=width,align='center',alpha=1,  color=color[1], label='toa do z')
plt.bar(ind - width,t, width=width,align='center',alpha=1,  color=color[2], label='toa do t')
plt.xlabel('toa do x', fontsize=20)
plt.ylabel('toa do y', fontsize=20)
plt.title('DO tuoi trung cua cac nuoc')
plt.grid(True)
plt.xticks(ind,x)
plt.ylim(0,120)
plt.legend()
plt.show()
```
Kết quả: 
<image src="../tim hieu ve matplotlib/vidu.png">   
- biểu đồ trên là biểu đồ với nhiều mảng giá trị khác nhau(y,z,t) được biểu diễn trong cùng một đồ thị, ứng với mỗi mảng có một màu ( y-red, z-green,t-blue).
- các cột của z và t được căn chỉnh so với tọa độ lần lượt là ind + width và ind - width.
- sử dụng plt.ylim(0,120) để giới hạn ymin=0 và ymax=120. (có thể làm tương tự đối với x -vd: plt.xlim(0,10))
- các câu lệnh còn lại đã được giải thích ở phía trên.






