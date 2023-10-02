'''We will implement all famous sorting algorithms as part of one class here
'''


class sortingmix:

    def __init__(self,array):

        self.array=array

    def selection_sort(self):

        arr=self.array

        for i in range(0,len(arr)):
            min_arr=arr[i]
            min_index=i
            for j in range(i+1,len(arr)):
                
                if arr[j]<min_arr:
                    min_arr=arr[j]
                    min_index=j
            arr[min_index]=arr[i]
            arr[i]=min_arr
        
        return arr
    def bubble_sort(self):

        arr=self.array

        n=len(arr)
        for i in range(n):
            
            for j in range(n-1,i,-1):
                
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
        return arr
    def insertion_sort(self):
        
        arr=self.array
        for i in range(len(arr)):
        
            temp=arr[i]
            j=i-1                         
            while j>=0 and arr[j]>temp:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                j-=1
            
        return arr

arra=[5, 8, 3, 9, 4, 1, 7]  
sorti=sortingmix(arra)

breakpoint()