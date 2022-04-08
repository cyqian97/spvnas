FROM mpirun_torch:1.8.2

RUN mkdir /dataset
RUN pip install mayavi numba opencv-python torchpack              
RUN pip install --upgrade git+https://github.com/mit-han-lab/torchsparse.git   
RUN git clone https://github.com/cyqian97/spvnas.git

CMD [ "zsh" ]

