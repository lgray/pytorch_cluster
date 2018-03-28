import pytest
import torch
from torch_cluster.functions.utils.degree import node_degree


def test_node_degree_cpu():
    row = torch.LongTensor([0, 1, 1, 0, 0, 3, 0])
    expected_degree = [4, 2, 0, 1]

    degree = node_degree(row, 4)
    assert degree.type() == torch.LongTensor().type()
    assert degree.tolist() == expected_degree

    degree = node_degree(row, 4, out=torch.FloatTensor())
    assert degree.type() == torch.FloatTensor().type()
    assert degree.tolist() == expected_degree


@pytest.mark.skipif(not torch.cuda.is_available(), reason='no CUDA')
def test_node_degree_gpu():  # pragma: no cover
    row = torch.cuda.LongTensor([0, 1, 1, 0, 0, 3, 0])
    expected_degree = [4, 2, 0, 1]

    degree = node_degree(row, 4)
    assert degree.type() == torch.cuda.LongTensor().type()
    assert degree.cpu().tolist() == expected_degree

    degree = node_degree(row, 4, out=torch.cuda.FloatTensor())
    assert degree.type() == torch.cuda.FloatTensor().type()
    assert degree.cpu().tolist() == expected_degree
