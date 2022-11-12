from helpers import create_forward_idx, create_inverse_idx, search_inverse_idx, search_forward_idx

if(__name__ == '__main__'):
    forward_index = create_forward_idx()
    inverse_index = create_inverse_idx()

    print('forward', forward_index, '\n')
    print('inverse', inverse_index, '\n')

    res_forward = search_forward_idx(forward_index, 'drow_ranger')
    res_inverse = search_inverse_idx(inverse_index, 'drow_ranger')

    print('res_forward', res_forward)
    print('res_inverse', res_inverse)
