#ifndef THC_GENERIC_FILE
#define THC_GENERIC_FILE "generic/THCGreedy.cu"
#else

void THCGreedy_(cluster)(THCState *state,
                         THCudaLongTensor *cluster,
                         THCudaLongTensor *row,
                         THCudaLongTensor *col,
                         THCudaLongTensor *deg,
                         THCTensor *weight) {
  printf("THCGreedy_cluster dynamic drin");
}

#endif  // THC_GENERIC_FILE


